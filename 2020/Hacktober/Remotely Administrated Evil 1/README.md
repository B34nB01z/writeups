# Remotely Administrated Evil 1

![Traffic Analysis](https://img.shields.io/badge/Traffic+Analysis--2e00ff?style=for-the-badge) ![Points - 20](https://img.shields.io/badge/Points-20-9cf?style=for-the-badge)

```txt
What is the name of the executable in the malicious url? Submit the filename as the flag: flag{virus.bad}.

file: https://tinyurl.com/y4z72k5o
SHA1: 0416385659fc307272b3494df067f6fa2ecc937437a24a75af7c86b666bce139 Password: hacktober
```

---

Essentially the same applies as for [`Evil Corp's Child 1`](../Evil%20Corp's%20Child%201/README.md). Apply a simple filter for HTTP traffic and, in this case, it will actually already be enough to give you the first flag:

![Wireshark](wireshark.png)

... the flag is: `flag{solut.exe}`