# Talking to the Dead 1

![Linux](https://img.shields.io/badge/Linux--ff00ff?style=for-the-badge) ![Points - 30](https://img.shields.io/badge/Points-30-9cf?style=for-the-badge)

```txt
We've obtained access to a server maintained by spookyboi. There are four flag files that we need you to read and submit (flag1.txt, flag2.txt, etc). Submit the contents of flag1.txt.

ssh hacktober@env.hacktober.io
Password: hacktober-Underdog-Truth-Glimpse
```

---

This first of these challenges was fairly trivial. Simply use the `find` command to list all possible `flag.txt` files:

```bash
find / -regextype sed -regex ".*flag.*\.txt" 2>/dev/null
```

```txt
/home/luciafer/Documents/.flag2.txt
/home/luciafer/Documents/flag1.txt
/home/spookyboi/Documents/flag3.txt
/root/flag4.txt
```

Now... you can actually just `cat` the contents of the `flag1.txt` file giving you the flag: `flag{cb07e9d6086d50ee11c0d968f1e5c4bf1c89418c}`