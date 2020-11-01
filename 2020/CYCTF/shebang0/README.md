# shebang0

![Shebang](https://img.shields.io/badge/Shebang--ff00ff?style=for-the-badge) ![Points - 125](https://img.shields.io/badge/Points-125-9cf?style=for-the-badge)

```txt
Welcome to the Shebang Linux Series. Here you will be tested on your basic command line knowledge! These challenges will be done threough an ssh connection. Also please do not try and mess up the challenges on purpose, and report any problems you find to the challenge author. The username is the challenge title, shebang0-6, and the password is the previous challenges flag, but for the first challenge, its shebang0
The first challenge is an introductory challenge. Connect to cyberyoddha.baycyber.net on port 1337 to recieve your flag!
- stephencurry396#4738
```

---

The first one of these challenges was still fairly trivial to solve. Simply connect to the server given in the task statement, list all files in the users home directory and cat the flag:

```bash
ssh shebang0@cyberyoddha.baycyber.net -p1337
ls -la
cat .flag.txt
```

... _tadaa_, here you go: `CYCTF{w3ll_1_gu3$$_b@sh_1s_e@zy}`
