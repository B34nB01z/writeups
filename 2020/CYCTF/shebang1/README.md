# shebang1

![Shebang](https://img.shields.io/badge/Shebang--ff00ff?style=for-the-badge) ![Points - 125](https://img.shields.io/badge/Points-125-9cf?style=for-the-badge)

```txt
This challenge is simple.

- stephencurry396#4738
```

---

The task description is not wrong ^^. Simply connect via SSH, cat flag.txt and grep for `CYCTF`:

```bash
ssh shebang1@cyberyoddha.baycyber.net -p1337
/bin/bash
ls -la
cat flag.txt | grep CYCTF
```

... this will give you: `CYCTF{w3ll_1_gu3$$_y0u_kn0w_h0w_t0_gr3p}`
