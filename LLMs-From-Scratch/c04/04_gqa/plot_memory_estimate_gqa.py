# Plot the KV_Cache vs context length for different n_kv_groups

import matplotlib.pyplot as plt

# Import from ./memory_estimator_gqa.py
from memory_estimator_gqa import kv_bytes_total, DTYPE_BYTES


def bytes_convert(n):
    gb = n / (1000 ** 3)
    return f"{gb:.2f}"


def savings_percent(total_mha, total_gqa):
    return (1.0 - (total_gqa / total_mha)) * 100.0


def plot_abs_kv_vs_context_multi_groups():
    n_heads = 24
    emb_dim = 2048
    n_layers = 48
    batch_size = 1
    dtype = "bf16"
    bytes_per_elem = DTYPE_BYTES[dtype]

    context_lengths = [
        256, 512, 1024, 2048, 4096,
        8192, 16384, 32768, 65536, 131072
    ]

    plt.figure()

    # ---- MHA ----
    mha_gb = []
    for L in context_lengths:
        total_mha = kv_bytes_total(
            batch_size, L, emb_dim, n_heads,
            n_heads,  # MHA
            n_layers, bytes_per_elem
        )
        mha_gb.append(float(bytes_convert(total_mha)))

    plt.plot(context_lengths, mha_gb, marker="o", label="MHA (KV total)")

    # ---- GQA ----
    groups_list = [4, 8, 12, 24]
    for g in groups_list:
        n_kv_heads = n_heads // g
        gqa_gb = []

        for L in context_lengths:
            total_gqa = kv_bytes_total(
                batch_size, L, emb_dim, n_heads,
                n_kv_heads, n_layers, bytes_per_elem
            )
            gqa_gb.append(float(bytes_convert(total_gqa)))

        comp = n_heads / n_kv_heads
        plt.plot(
            context_lengths, gqa_gb, marker="o",
            label=f"GQA (n_kv_groups={g}, {comp:,.1f}x compression)"
        )

    plt.xscale("log")
    plt.xlabel("context_length (log scale)")
    plt.ylabel("Total KV cache (GB)")
    plt.title(
        "KV-cache vs Context Length — MHA vs GQA (multi-group)\n"
        "(n_heads=24, emb_dim=2048, n_layers=48, batch=1, dtype=bf16)",
        fontsize=8
    )

    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("kv_bytes_vs_context_length.pdf")


if __name__ == "__main__":
    plot_abs_kv_vs_context_multi_groups()
