# shebang4

![Shebang](https://img.shields.io/badge/Shebang--ff00ff?style=for-the-badge) ![Points - 200](https://img.shields.io/badge/Points-200-9cf?style=for-the-badge)

```txt
Since you have been doing so well, I thought I would make this an easy one.

- stephencurry396#4738
```

---

Ok... this challenge's focus was on transferring the image file on the server to your local PC. We just used base64 to achieve that:

```bash
cat flag.png | base64
```

... now... copy the output and decode it on your own PC:

```bash
echo '<copied_base64>' | base64 -d > flag.png
```

... simply take a look at the image now:

![flag](./flag.png)

... the flag is: `CYCTF{W3ll_1_gu3$$_th@t_w@s_actually_easy}`
