<div align="center">
    <h1>Phasestream4</h1>
    <img src="https://img.shields.io/badge/category-crypto-e8ff00" /> <img src="https://img.shields.io/badge/points-300-eaeaea" />
</div>

---

```txt
The aliens saw us break PhaseStream 3 and have proposed a quick fix to protect their new cipher.
This challenge will raise 43 euros for a good cause.
```

---

Restore beginning of quote by xoring it with flag prefix `CHTB{` --> `I alo`. Considering the quote from the previous challenge was real, search for quotes starting with `I alo`. This leads you to [Mother Teresa](https://www.goodreads.com/quotes/49502-i-alone-cannot-change-the-world-but-i-can-cast).

> I alone cannot change the world, but I can cast a stone across the waters to create many ripples.

This one has a slight typo in it it should be "water" and not "waters". Use this to restore the keystream and xor it with the encrypted flag to get the plaintext flag: 

<h4 align="center">
    CHTB{stream_ciphers_with_reused_keystreams_are_vulnerable_to_known_plaintext_attacks}
</h4>