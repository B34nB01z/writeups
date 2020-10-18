# Evil Twin

![Forensics](https://img.shields.io/badge/Forensics--blueviolet?style=for-the-badge) ![Points - 150](https://img.shields.io/badge/Points-150-9cf?style=for-the-badge)

```txt
One of the junior analysts thinks that there is a duplicate process - an "evil twin" - masquerading as a legitimate process. What is the name of the malicious process?  Submit the flag as flag{process_name.ext}

Use the file from Captured Memories.
Max Attempts: 5
```

---

Still using the memory dump from [`Captured Memories`](../Captured%20Memories/README.md) it was now time to discover an _imposter process_ - a process that carries the name of a normal, well-known windows application, yet does something entirely different and usually malicious.

Well... how do we go about doing that? The first thing we did, was to execute a regular `pstree` command to have an easier overview over the parent-child relationships in the dump.

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

Nothing too suspicious here... Let's do the classical thing to identify malicious duplicates - let's see what process are communicating on the network:

```bash
python2.7 vol.py -f mem.raw --profile=Win10x64_15063 netscan
```

```txt
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x87868e8f8070     TCPv4    192.168.1.99:50464             192.168.1.157:4455   ESTABLISHED      -1                      
0x87868ed197d0     UDPv6    fe80::4fc:695a:ef20:7868:1900  *:*                                   4804     svchost.exe    2020-06-26 15:33:05 UTC+0000
0x87868ecceec0     TCPv4    0.0.0.0:6666                   0.0.0.0:0            LISTENING        5448     explorer.exe   2020-06-26 15:43:14 UTC+0000
0x87868edb4cc0     TCPv6    ::1:50505                      ::1:445              CLOSED           -1                      -
0x87868ef2ac80     UDPv4    0.0.0.0:64088                  *:*                                   5736     chrome.exe     2020-06-26 15:51:01 UTC+0000
...                ...      ...                            ...                  ...              ...      ...            ...
0x87869163eeb0     UDPv6    :::58924                       *:*                                   5736     chrome.exe     2020-06-26 15:51:04 UTC+0000
0x878691658cc0     TCPv6    ::1:445                        ::1:50505            CLOSED           -1                      
0x8786916e4e60     UDPv4    127.0.0.1:1900                 *:*                                   4804     svchost.exe    2020-06-26 15:33:05 UTC+0000
0xb00ecc9dacc0     TCPv6    2600:6c42:7800:1415:9d41:eaa5:82a3:cce:50490 2620:1ec:c11::200:443 CLOSED           -1                      -
0xd380000b3010     TCPv6    2600:6c42:7800:1415:9d41:eaa5:82a3:cce:50498 2620:1ec:bdf::254:443 CLOSED           -1                      
```

... well... i don't think `explorer.exe` usually opens up ports... ^^. We've found the _Evil Twin_ - the flag therfore is: `flag{explorer.exe}`.