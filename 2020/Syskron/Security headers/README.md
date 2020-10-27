# Security headers

![Web](https://img.shields.io/badge/Web--0042ff?style=for-the-badge) ![Points - 100](https://img.shields.io/badge/Points-100-9cf?style=for-the-badge)

```txt
Can you please check the security-relevant HTTP response headers on www.senork.de. Do they reflect current best practices?
```

---

One of the easier web challenges. Simply take a look at the response headers the web server sends you when you request the page.

Here you'll find one interesting one: `Flag-Policy`. The value is the flag: `syskronCTF{y0u-f0und-a-header-flag}`
