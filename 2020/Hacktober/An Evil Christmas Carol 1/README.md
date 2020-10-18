# An Evil Christmas Carol 1

![Traffic Analysis](https://img.shields.io/badge/Traffic+Analysis--2e00ff?style=for-the-badge) ![Points - 20](https://img.shields.io/badge/Points-20-9cf?style=for-the-badge)

```txt
A malicious dll was downloaded over http in this traffic, what was the ip address that delivered this file?

file: https://tinyurl.com/y259doyq
SHA1: 7659667a17bca60310043014ad7971130780cbc1
Password: hacktober
```

---

Pretty much the same as in both other entry-level traffic analysis challenges: Just filter for HTTP traffic!

![Wireshark](wireshark.png)

... as this will (at least in this case) already present you with the flag: `flag{205.185.125.104}`