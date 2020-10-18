# An Evil Christmas Carol 2

![Traffic Analysis](https://img.shields.io/badge/Traffic+Analysis--2e00ff?style=for-the-badge) ![Points - 50](https://img.shields.io/badge/Points-50-9cf?style=for-the-badge)

```txt
What is the domain used by the post-infection traffic over HTTPS?
Use the file from An Evil Christmas Carol.
```

---

_This challenge is **very** similar to [`Remotely Administrated Evil 2`](../Remotely%20Administrated%20Evil%202/README.md), so I suggest you take a look at that first!_

From the last stage of this challenge, you still have the IP address of the _infected client_ (`10.0.0.163`). Now, simply look at all DNS queries this client has made:

![Wireshark](./wireshark.png)

... one should really stick out! This is already the flag: `flag{vlcafxbdjtlvlcduwhga.com}`