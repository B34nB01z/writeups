# Talking to the Dead 2

![Linux](https://img.shields.io/badge/Linux--ff00ff?style=for-the-badge) ![Points - 30](https://img.shields.io/badge/Points-30-9cf?style=for-the-badge)

```txt
There's a hidden flag that belongs to luciafer. Submit the contents of the hidden flag2.txt.

ssh hacktober@env.hacktober.io
Password: hacktober-Underdog-Truth-Glimpse
```

---

_Read [`Talking to the Dead 1`](../Talking%20to%20the%20Dead%201/README.md) first!_

Well... if you take another look at the output of the `find` command from the last challenge again - you'll already find the second hidden flag:

```txt
/home/luciafer/Documents/.flag2.txt
/home/luciafer/Documents/flag1.txt
/home/spookyboi/Documents/flag3.txt
/root/flag4.txt
```

... the challenge being that, had you simply used a regular `ls` (without the `-a` flag), you'd not have seen the "hidden" file. But... there are no further protections... simply `cat` the flag: `flag{728ec98bfaa302b2dfc2f716d3de7869f3eadcbf}`
