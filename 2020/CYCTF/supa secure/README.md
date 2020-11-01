# supa secure

![Password-cracking](https://img.shields.io/badge/Password%20cracking--780707?style=for-the-badge) ![Points - 225](https://img.shields.io/badge/Points-225-9cf?style=for-the-badge)

```txt
This time it’s a little tricker to crack the password: 19d14c463333a41a1538dbf9eb76aadf
You might also need this for something: cyctf
Are you up for the challenge?
- Haskell#1426
```

---

This suggests, that `cyctf` is the Salt? Also the Hash looked like MD5

However, using [MD5Online](https://www.md5online.org/md5-decrypt.html) gave us this: `ilovesalt`

`CYCTF{ilovesalt}`

