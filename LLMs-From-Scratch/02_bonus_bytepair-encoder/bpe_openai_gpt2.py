
# -*- coding: utf-8 -*

import os
import json
import regex as re
import requests
from tqdm import tqdm
from functools import lru_cache


@lru_cache()
def bytes_to_unicode():
    """
    Returns a reversible mapping between bytes (0..255) and unicode characters.
    """
    bs = list(range(ord("!"), ord("~") + 1)) \
         + list(range(ord("¡"), ord("¬") + 1)) \
         + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(2**8):
        if b not in bs:
            bs.append(b)
            cs.append(2**8 + n)
            n += 1
    cs = [chr(n) for n in cs]
    return dict(zip(bs, cs))


def get_pairs(word):
    """Return set of symbol pairs in a word (word is a tuple of symbols)."""
    pairs = set()
    prev_char = word[0]
    for char in word[1:]:
        pairs.add((prev_char, char))
        prev_char = char
    return pairs


class Encoder:
    def __init__(self, encoder, bpe_merges, errors="replace"):
        self.encoder = encoder
        self.decoder = {v: k for k, v in self.encoder.items()}
        self.errors = errors
        self.byte_encoder = bytes_to_unicode()
        self.byte_decoder = {v: k for k, v in self.byte_encoder.items()}
        # bpe_merges is a list of tuples like [('l', 'o'), ('lo', 'w'), ...]
        self.bpe_ranks = dict(zip(bpe_merges, range(len(bpe_merges))))
        self.cache = {}

        # tokenization regex (keeps contractions and words/numbers/punctuation/spaces)
        self.pat = re.compile(
            r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s""",
            re.IGNORECASE,
        )

    def bpe(self, token):
        """Apply BPE to a token (string of unicode "bytes" produced by byte_encoder)."""
        if token in self.cache:
            return self.cache[token]

        # work with tuple of characters/symbols
        word = tuple(token)
        pairs = get_pairs(word)

        if not pairs:
            self.cache[token] = token
            return token

        # main merge loop: pick lowest-rank bigram and merge all its occurrences
        while True:
            pairs = get_pairs(word)
            if not pairs:
                break

            # find the highest-priority bigram (lowest rank number)
            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float("inf")))

            # if this bigram isn't in the merges, stop
            if bigram not in self.bpe_ranks:
                break

            first, second = bigram
            new_word = []
            i = 0
            L = len(word)
            while i < L:
                # try to find the next occurrence of `first` starting from i
                try:
                    j = word.index(first, i)
                except ValueError:
                    # no more occurrences; append the rest and break
                    new_word.extend(word[i:])
                    break

                # append the symbols between i and j
                new_word.extend(word[i:j])

                # if the bigram matches at j (i.e., next symbol is `second`), merge
                if j < L - 1 and word[j + 1] == second:
                    new_word.append(first + second)
                    i = j + 2
                else:
                    # otherwise just append the symbol at j and continue searching after it
                    new_word.append(word[j])
                    i = j + 1

            word = tuple(new_word)
            if len(word) == 1:
                break

        word_str = " ".join(word)
        self.cache[token] = word_str
        return word_str

    def encode(self, text):
        """Encode text -> list of token ids (using self.encoder mapping)."""
        bpe_tokens = []
        for token in re.findall(self.pat, text):
            # map each byte of utf-8 encoding to the corresponding unicode-char mapping
            token_bytes = token.encode("utf-8")
            token = "".join(self.byte_encoder[b] for b in token_bytes)
            bpe_piece = self.bpe(token)
            for bpe_token in bpe_piece.split(" "):
                if bpe_token in self.encoder:
                    bpe_tokens.append(self.encoder[bpe_token])
                else:
                    # If token missing in encoder dict, raise or handle (here we raise)
                    raise KeyError(f"Token '{bpe_token}' not found in encoder vocabulary.")
        return bpe_tokens

    def decode(self, tokens):
        """Decode list of token ids -> text."""
        text = "".join(self.decoder[token] for token in tokens)
        byte_array = bytearray([self.byte_decoder[c] for c in text])
        text = byte_array.decode("utf-8", errors=self.errors)
        return text


def get_encoder(model_name, models_dir):
    enc_path = os.path.join(models_dir, model_name, "encoder.json")
    bpe_path = os.path.join(models_dir, model_name, "vocab.bpe")

    with open(enc_path, "r", encoding="utf-8") as f:
        encoder = json.load(f)

    with open(bpe_path, "r", encoding="utf-8") as f:
        bpe_data = f.read()

    # first line is a header, merges follow; ignore empty lines
    merges = [tuple(line.split()) for line in bpe_data.split("\n")[1:] if line.strip()]
    return Encoder(encoder=encoder, bpe_merges=merges)


def download_vocab(target_dir="gpt2-model"):
    """
    Downloads encoder.json and vocab.bpe from the 117M GPT-2 hosted files
    into the given target directory.
    """
    os.makedirs(target_dir, exist_ok=True)
    # safe windows path normalization
    subdir = target_dir.replace("\\", "/")

    base_url = "https://openaipublic.blob.core.windows.net/gpt-2/models/117M/"
    filenames = ["encoder.json", "vocab.bpe"]

    for filename in filenames:
        url = base_url + filename
        resp = requests.get(url, stream=True)
        resp.raise_for_status()

        out_path = os.path.join(subdir, filename)
        file_size = int(resp.headers.get("content-length", 0))
        chunk_size = 1024

        with open(out_path, "wb") as f, tqdm(
            ncols=100, desc=f"Fetching {filename}", total=file_size, unit="B", unit_scale=True
        ) as pbar:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if not chunk:
                    continue
                f.write(chunk)
                pbar.update(len(chunk))
    return True
