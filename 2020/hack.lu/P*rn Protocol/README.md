# P*rn Protocol

![Misc](https://img.shields.io/badge/Misc--ff0049?style=for-the-badge) ![Points - 190](https://img.shields.io/badge/Points-190-9cf?style=for-the-badge)

```txt
I know you want it. But please don't talk dirty to me. 

nc flu.xxx 2005 
files: https://pwnhub.fluxfingers.net/static/chall/prnprotocol_abea9f87630a37c0209bb35a8f6ad847.zip
```

---

## TL;DR

... actually... there isn't too much to explain here ... ^^ All you had to do was to implement the protocol described in the [provided PDF](public/Documentation.pdf) to then use this implementation to retrieve the flag.

Ok, here's a short summary of what our final implementation [main.py](./main.py) essentially does:

1. it requests a `member id` (username, password) from the server.
2. it then uses these credentials together with a `login` request to _"authenticate"_ at the server.
3. it requests the flag and, on success, prints it to the terminal.

If you code such a script yourself or use the one attached, you'll end up with the flag: `flag{vpns_ar3_n0t_h4ck3r_appr0v3d}`
