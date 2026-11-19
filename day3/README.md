# Tokens

A **token** is a small chunk of text that a language model actually works with.
When you send a prompt, the model does not read the raw words or characters —
it first converts the text into a sequence of numbers (token IDs), one per token.

A token can be:
- a whole word (e.g. `Hello`, `The`),
- a common word-part (e.g. `ing`, `tion`, `un`, `able`),
- or even a single character.

---

## Why do we need tokens?

- If the model worked with **raw characters**, every sentence would turn into a very
  long sequence of numbers (one per letter) — the input becomes huge and hard to process.
- If the model worked with **whole words**, the vocabulary would grow without limit —
  new words, typos, and rare words would never have an entry.
- **Tokens solve both problems**: the vocabulary is a fixed, manageable list
  (typically tens of thousands of entries), and any text can be expressed as a compact
  sequence of IDs taken from that list.

---

## How does the model know the mapping?

During training, the tokenizer builds a **fixed vocabulary** — a dictionary that maps
each token string to a unique number. This mapping is learned **once** and stays the same.
It does **not** scan the internet live, and it does **not** store a dictionary of words in memory.

When you ask the model something, it simply looks up your prompt in that fixed table and
breaks it into tokens.

---

## Example

> The apple is Cranda.

becomes something like:

```
[The] [apple] [is] [Cr] [anda] [.]   →   6 tokens
```

Note: the exact split depends on the model's vocabulary. Common words like **"The"**,
**"apple"**, and **"is"** are usually a single token each, but a made-up word like
**"Cranda"** is *not* in the vocabulary, so the model breaks it into subword pieces
instead — for example `Cr` + `anda` — which makes it **2 tokens**, not 1. The period
`.` is also its own token. That is why a sentence of 5 words can become 6 tokens.

---

## Quick summary

| Idea | Correct version |
|------|-----------------|
| Token = a common reusable word | A subword piece: whole word, word-part, or single character |
| Model breaks text into ASCII numbers | Model breaks text into **IDs from a fixed vocabulary** |
| Model scans the internet and saves words | Vocabulary is **fixed at training time**; it's a static lookup table |
| Tokens exist to avoid huge inputs | Tokens exist so the vocabulary stays **fixed and manageable** |

## Tokenization — how text becomes tokens

**Tokenization** is the process of turning raw text into a sequence of tokens.
It happens *before* the model ever sees the input, and it is the step that decides
how your prompt will be broken up.

### How it works (roughly)

1. Start with your text: `The apple is Cranda.`
2. The tokenizer tries to match the **longest possible pieces** it already knows.
3. It looks up each piece in the vocabulary and replaces it with its ID number.
4. Whatever is left over — words or parts not in the vocabulary — gets split into
   smaller and smaller pieces until everything is covered.
5. The result is a list of token IDs, which is what the model actually receives.

### Example

```
Input:  "The apple is Cranda."
Tokens: [The] [apple] [is] [Cr] [anda] [.]      → 6 tokens
IDs:    464   2068    374  1234  5678   262
```

Notice that the made-up word **"Cranda"** is not in the vocabulary, so instead of
one token it becomes **two** — `Cr` + `anda`. That's why a prompt's token count is
not simply its word count.

### Why it matters

- **Token count ≠ word count.** A long word, a URL, a piece of code, or a non-English
  word can each turn into several tokens.
- **Prompt length is measured in tokens**, not characters or words. If your prompt is
  too long, it gets cut off — the model can only handle so many tokens at once.
- **Punctuation and spaces count too.** Even a single period or a space can be its own
  token.

### The two common algorithms

- **BPE (Byte-Pair Encoding)** — used by GPT models. Starts from individual characters
  and repeatedly merges the most frequent pairs into bigger tokens.
- **WordPiece / SentencePiece** — used by BERT and T5 models. Builds a vocabulary that
  maximizes the likelihood of the training text.


