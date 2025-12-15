import argparse
import time
import tiktoken
import torch
import torch.nn as nn



##############################################
# Grouped-Query Attention (GQA)
##############################################
class GroupedQueryAttention(nn.Module):
    def __init__(
        self,
        d_in,
        d_out,
        dropout,
        num_heads,
        num_kv_groups,
        qkv_bias=False,
        dtype=None,
    ):
        super().__init__()

        assert d_out % num_heads == 0, "d_out must be divisible by num_heads"
        assert num_heads % num_kv_groups == 0, "num_heads must be divisible by num_kv_groups"

        self.d_out = d_out
        self.num_heads = num_heads
        self.num_kv_groups = num_kv_groups
        self.group_size = num_heads // num_kv_groups
        self.head_dim = d_out // num_heads

        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias, dtype=dtype)
        self.W_key = nn.Linear(d_in, num_kv_groups * self.head_dim, bias=qkv_bias, dtype=dtype)
        self.W_value = nn.Linear(d_in, num_kv_groups * self.head_dim, bias=qkv_bias, dtype=dtype)

        self.out_proj = nn.Linear(d_out, d_out, dtype=dtype)
        self.dropout = nn.Dropout(dropout)

        self.register_buffer("cache_k", None, persistent=False)
        self.register_buffer("cache_v", None, persistent=False)
        self.ptr_current_pos = 0

    def forward(self, x, use_cache=False):
        b, t, _ = x.shape

        q = self.W_query(x)
        k = self.W_key(x)
        v = self.W_value(x)

        q = q.view(b, t, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(b, t, self.num_kv_groups, self.head_dim).transpose(1, 2)
        v = v.view(b, t, self.num_kv_groups, self.head_dim).transpose(1, 2)

        if use_cache:
            if self.cache_k is None:
                self.cache_k, self.cache_v = k, v
            else:
                self.cache_k = torch.cat([self.cache_k, k], dim=2)
                self.cache_v = torch.cat([self.cache_v, v], dim=2)
            k_base, v_base = self.cache_k, self.cache_v
        else:
            k_base, v_base = k, v
            self.cache_k, self.cache_v = None, None
            self.ptr_current_pos = 0

        k = k_base.repeat_interleave(self.group_size, dim=1)
        v = v_base.repeat_interleave(self.group_size, dim=1)

        attn_scores = q @ k.transpose(2, 3)

        tq = q.size(-2)
        tk = k.size(-2)
        device = q.device

        if use_cache:
            q_pos = torch.arange(self.ptr_current_pos, self.ptr_current_pos + tq, device=device)
            self.ptr_current_pos += tq
        else:
            q_pos = torch.arange(tq, device=device)

        k_pos = torch.arange(tk, device=device)
        causal_mask = q_pos.unsqueeze(-1) < k_pos.unsqueeze(0)

        attn_scores = attn_scores.masked_fill(causal_mask, -torch.inf)
        attn_weights = torch.softmax(attn_scores / (self.head_dim ** 0.5), dim=-1)
        attn_weights = self.dropout(attn_weights)

        context = (attn_weights @ v).transpose(1, 2)
        context = context.contiguous().view(b, tq, self.d_out)
        return self.out_proj(context)

    def reset_cache(self):
        self.cache_k, self.cache_v = None, None
        self.ptr_current_pos = 0


##############################################
# Transformer blocks
##############################################
class LayerNorm(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.eps = 1e-5
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        return self.scale * (x - mean) / torch.sqrt(var + self.eps) + self.shift


class GELU(nn.Module):
    def forward(self, x):
        return 0.5 * x * (1 + torch.tanh(
            torch.sqrt(torch.tensor(2.0 / torch.pi, device=x.device)) *
            (x + 0.044715 * x ** 3)
        ))


class FeedForward(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(cfg["emb_dim"], 4 * cfg["emb_dim"]),
            GELU(),
            nn.Linear(4 * cfg["emb_dim"], cfg["emb_dim"]),
        )

    def forward(self, x):
        return self.net(x)


class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = GroupedQueryAttention(
            d_in=cfg["emb_dim"],
            d_out=cfg["emb_dim"],
            num_heads=cfg["n_heads"],
            num_kv_groups=cfg["n_kv_groups"],
            dropout=cfg["drop_rate"],
            qkv_bias=cfg["qkv_bias"],
        )
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
        self.drop = nn.Dropout(cfg["drop_rate"])

    def forward(self, x, use_cache=False):
        x = x + self.drop(self.att(self.norm1(x), use_cache=use_cache))
        x = x + self.drop(self.ff(self.norm2(x)))
        return x


##############################################
# GPT Model
##############################################
class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.tok_emb = nn.Embedding(cfg["vocab_size"], cfg["emb_dim"])
        self.pos_emb = nn.Embedding(cfg["context_length"], cfg["emb_dim"])
        self.drop = nn.Dropout(cfg["drop_rate"])

        self.blocks = nn.ModuleList([TransformerBlock(cfg) for _ in range(cfg["n_layers"])])
        self.norm = LayerNorm(cfg["emb_dim"])
        self.head = nn.Linear(cfg["emb_dim"], cfg["vocab_size"], bias=False)

        self.current_pos = 0

    def forward(self, idx, use_cache=False):
        b, t = idx.shape
        tok = self.tok_emb(idx)

        if use_cache:
            pos_ids = torch.arange(self.current_pos, self.current_pos + t, device=idx.device)
            self.current_pos += t
        else:
            pos_ids = torch.arange(t, device=idx.device)
            self.current_pos = 0

        x = self.drop(tok + self.pos_emb(pos_ids).unsqueeze(0))
        for blk in self.blocks:
            x = blk(x, use_cache=use_cache)
        return self.head(self.norm(x))

    def reset_kv_cache(self):
        for blk in self.blocks:
            blk.att.reset_cache()
        self.current_pos = 0


##############################################
# Text generation
##############################################
def generate_text_simple_cached(model, idx, max_new_tokens, use_cache=True):
    model.eval()
    with torch.no_grad():
        if use_cache:
            model.reset_kv_cache()
            logits = model(idx, use_cache=True)
            for _ in range(max_new_tokens):
                next_token = logits[:, -1].argmax(dim=-1, keepdim=True)
                idx = torch.cat([idx, next_token], dim=1)
                logits = model(next_token, use_cache=True)
        else:
            for _ in range(max_new_tokens):
                logits = model(idx)
                next_token = logits[:, -1].argmax(dim=-1, keepdim=True)
                idx = torch.cat([idx, next_token], dim=1)
    return idx


##############################################
# Main
##############################################
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_new_tokens", type=int, default=200)
    args = parser.parse_args()

    cfg = {
        "vocab_size": 50257,
        "context_length": 1024,
        "emb_dim": 768,
        "n_heads": 12,
        "n_layers": 12,
        "n_kv_groups": 2,
        "drop_rate": 0.0,
        "qkv_bias": False,
    }

    tokenizer = tiktoken.get_encoding("gpt2")
    start_text = "Hello, I am"
    idx = torch.tensor(tokenizer.encode(start_text)).unsqueeze(0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GPTModel(cfg).to(device)
    idx = idx.to(device)

    start = time.time()
    out = generate_text_simple_cached(model, idx, args.max_new_tokens)
    elapsed = time.time() - start

    print(tokenizer.decode(out[0].tolist()))
    print(f"Time: {elapsed:.2f}s | Tokens/sec: {out.size(1) / elapsed:.1f}")


if __name__ == "__main__":
    main()
