# Hell Spawn 1

![Forensics](https://img.shields.io/badge/Forensics--blueviolet?style=for-the-badge) ![Points - 100](https://img.shields.io/badge/Points-100-9cf?style=for-the-badge)

```
What was the name of the process that spawned the malicious explorer.exe? Submit the flag as the name and extension of the process and the PID of the process, separated by an underscore: flag{process_name.ext_PID}

Use the file from Captured Memories.
Max attempts: 10
```

---

Another continuation of the [`Captured Memories`](../Captured%20Memories/README.md) memory dump. Considering that we already know the name + PID of the malicious process (from the [`Evil Twin`](../Evil%20Twin/README.md) challenge), we can simply take a look at the ouptut of the `pstree` command again:

```bash
python2.7 vol.py -f mem.raw --profile=Win10x64_15063 pstree
```

```txt
Volatility Foundation Volatility Framework 2.6.1
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xffff87868e88d440:System                              4      0    111      0 2020-06-26 15:07:32 UTC+0000
. 0xffff878690147040:smss.exe                         348      4      2      0 2020-06-26 15:07:32 UTC+0000
. 0xffff87868e975040:Registry                          88      4      3      0 2020-06-26 15:07:23 UTC+0000
. 0xffff878690ccc040:MemCompression                  1168      4     50      0 2020-06-26 15:07:58 UTC+0000
 0xffff878690495080:wininit.exe                       528    424      1      0 2020-06-26 15:07:45 UTC+0000
. 0xffff8786904cd080:services.exe                     648    528      6      0 2020-06-26 15:07:46 UTC+0000
                                                      ...    ...    ...    ... ...
... 0xffff878691456080:cmd.exe                       3944   4448      0 ------ 2020-06-26 15:37:19 UTC+0000
.... 0xffff87868fd63580:conhost.exe                  5432   3944      4      0 2020-06-26 15:37:19 UTC+0000
.... 0xffff878691762080:explorer.exe                 5448   3944      1      0 2020-06-26 15:43:14 UTC+0000
... 0xffff878691457580:cmd.exe                       4424   4448      1      0 2020-06-26 15:46:51 UTC+0000
.... 0xffff87868f773080:explorer.exe                 3100   4424      5      0 2020-06-26 15:48:21 UTC+0000
..... 0xffff87868f77b340:cmd.exe                     4640   3100      1      0 2020-06-26 15:48:21 UTC+0000
.... 0xffff87868f998080:conhost.exe                  6372   4424      3      0 2020-06-26 15:46:51 UTC+0000
                                                      ...    ...    ...    ... ...
 0xffff878691061580:GoogleCrashHan                   4332   2776      5      0 2020-06-26 15:10:38 UTC+0000
 0xffff8786910be080:GoogleCrashHan                   5936   2776      3      0 2020-06-26 15:10:38 UTC+0000
```

... and, as you can see, the malicious `explorer.exe` (PID `5448`) has the process `cmd.exe` (PID `3944`) as its parent. Therefore the flag had to be: `flag{cmd.exe_3944}`