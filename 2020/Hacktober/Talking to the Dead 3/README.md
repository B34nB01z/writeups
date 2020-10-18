# Talking to the Dead 3

![Linux](https://img.shields.io/badge/Linux--ff00ff?style=for-the-badge) ![Points - 100](https://img.shields.io/badge/Points-100-9cf?style=for-the-badge)

```txt
Submit the contents of flag3.txt from the remote machine.

ssh hacktober@env.hacktober.io
Password: hacktober-Underdog-Truth-Glimpse
```

---

_Read through [`Talking to the Dead 4`](../Talking%20to%20the%20Dead%204/README.md) first! (Yes, I mean the one that should technically come after this one ^^)_

Well... if you solve `Talking to the Dead 4` before this one... it's once again pretty trivial to get the flag ^^.

You can simply use the discovered `setuid` binary to also echo the `flag3.txt` file in the other user's home directory:

```bash
/usr/local/bin/ouija ../home/spookyboi/Documents/flag3.txt
```

_Altough, to be fair, the straight forward method of passing `/home/spookyboi/Documents/flag3.txt` doesn't work ^^_

... anyways... this gives you the third flag: `flag{445b987b5b80e445c3147314dbfa71acd79c2b67}`