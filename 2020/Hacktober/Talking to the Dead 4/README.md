# Talking to the Dead 4

![Linux](https://img.shields.io/badge/Linux--ff00ff?style=for-the-badge) ![Points - 300](https://img.shields.io/badge/Points-300-9cf?style=for-the-badge)

```txt
We suspect spookyboi doesn't use the root account for this server. There must be some mechanism used to read the flag4.txt file without gaining root. Submit the contents of flag4.txt from the remote machine.

ssh hacktober@env.hacktober.io
Password: hacktober-Underdog-Truth-Glimpse
```

---

_Read [`Talking to the Dead 2`](../Talking%20to%20the%20Dead%202/README.md) first!_

Well, this is quite the step up from the last challenges, isn't it? From looking at the output of the `find` command used to solve the previous steps of this challenge series we know where the `flag4.txt` file is located:

```txt
/home/luciafer/Documents/.flag2.txt
/home/luciafer/Documents/flag1.txt
/home/spookyboi/Documents/flag3.txt
/root/flag4.txt
```

... however, this time it's located in the `/root` folder. Uh oh! No permissions for us:

```bash
ls -l /root/flag4.txt
```

```txt
-rw------- 1 root root 47 Oct  6 08:41 /root/flag4.txt
```

One little thing in the Linux world would allow us to read from this file, however, ... binaries with the `setuid` flag. These files will always (as the name of the flag suggests) be run with the owner's user id. So... if you somehow manage to get a shell with a `setuid` binary owned by `root`, you could do whatever you want with the system.

In this case, it was a little easier, however... Simply use find once again to search for fitting executables:

```bash
find / -perm /4000 2>/dev/null
```

_`2>/dev/null` is being used to hide error messages_

```txt
/usr/bin/umount
/usr/bin/passwd
/usr/bin/mount
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/chfn
/usr/local/bin/ouija
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
```

... and ... in the midst of all binaries that normally have the `setuid` flag, you find one very suspiciouis one: `/usr/local/bin/ouija`.

Simply executing this gives us the following usage message:

```txt
OUIJA 6.66 - Read files in the /root directory
Usage: ouija [FILENAME]
EXAMPLES:
	ouija file.txt
	ouija read.meluciafer@dee730b461da
```

... well... that was easier than thought ^^. Simply run the binary again, passing an appropriate argument: 

```bash
/usr/local/bin/ouija flag4.txt
```

... _tadaa_, you're presented with the flag! Amazing: `flag{4781cbffd13df6622565d45e790b4aac2a4054dc}`