# Captured Memories

![Forensics](https://img.shields.io/badge/Forensics--blueviolet?style=for-the-badge) ![Points - 30](https://img.shields.io/badge/Points-30-9cf?style=for-the-badge)

```txt
We found some unusual activity coming from an employee's Windows 10 workstation at De Monne Financial. Our IT guy saved the memory dump to the file provided below. What was the PID of the program used to capture the memory dump?  Submit the flag as flag{PID}.

link: https://tinyurl.com/y9r3wnhh
Max Attempts: 10
```

---

Since this challenge involves a memory dump, the tool you'll probably have the most success with is [volatility](https://www.volatilityfoundation.org/).

So... we didn't think much of it and ran a simple ...

```bash
volatility -f mem.raw imageinfo
```

... on the unzipped memory image - this did provide us with some results, although, suspiciously, there is no `instantiated with` - apparently volatility couldn't find a perfect match...

```txt
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win10x64_14393, Win10x64_10586, Win10x64, Win2016x64_14393
                     AS Layer1 : Win10AMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/mnt/d/hacking/Hacktober/2020/captured-memories/mem.raw)
                      PAE type : No PAE
                           DTB : 0x1aa000L
                          KDBG : 0xf8001e43d520L
          Number of Processors : 2
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff8001d4e2000L
                KPCR for CPU 1 : 0xffffd40032268000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-06-26 15:51:36 UTC+0000
     Image local date and time : 2020-06-26 08:51:36 -0700
```

We chose to ignore this at first and simply used the `Win10x64_10586` profile for now. Ok... now a simple `pslist` should tell us what process the task description was talking about... and...

```bash
volatility -f mem.raw --profile=Win10x64_10586 pslist
```

```txt
Volatility Foundation Volatility Framework 2.6
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xffff87868e88d438                           4      0 24...4        0 ------      0 6285-08-11 06:06:22 UTC+0000                                 
0xffff87868e975038                          88      0 24...8        0 ------      0 6228-07-11 06:16:00 UTC+0000                                 
0xffff878690147038  ??????smss.exe         348      0 24...2        0 ------      0 6235-10-10 13:14:27 UTC+0000                                 
...                 ...                     ...   ...    ...      ...    ...    ... ...
0xffff87868ebef078 ????????chrome.e       2512    540 24...4        0 ------      0 6236-07-21 07:00:39 UTC+0000                                 
0xffff87868f2e1078 ????????winpmem_       3348    332 23...6        0 ------      0 6236-07-21 07:00:39 UTC+0000                                 
```

... oh... umm... what happened? ^^ there seems to be a problem with the profiles after all (trust me, we tried the other ones as well, all produced such results). 

But... this is where one important trick with volatility comes into play: **Always** use the newest version - clone the github repo.

So... we went ahead and did that, tried the `imageinfo` command again, and ...

```txt
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win10x64_17134, Win10x64_14393, Win10x64_10586, Win10x64_16299, Win2016x64_14393, Win10x64_17763, Win10x64_15063 (Instantiated with Win10x64_15063)
                     AS Layer1 : SkipDuplicatesAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/mnt/d/hacking/Hacktober/2020/captured-memories/mem.raw)
                      PAE type : No PAE
                           DTB : 0x1aa000L
                          KDBG : 0xf8001e43d520L
          Number of Processors : 2
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff8001d4e2000L
                KPCR for CPU 1 : 0xffffd40032268000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-06-26 15:51:36 UTC+0000
     Image local date and time : 2020-06-26 08:51:36 -0700
```

... *boom* ^^, way more results + finally a recommended image: `Win10x64_15063`.

And... once we re-ran the `pslist` command...

```bash
python2.7 vol.py -f mem.raw --profile=Win10x64_15063 pslist
```

```txt
Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xffff87868e88d440 System                    4      0    111        0 ------      0 2020-06-26 15:07:32 UTC+0000                                 
0xffff87868e975040 Registry                 88      4      3        0 ------      0 2020-06-26 15:07:23 UTC+0000                                 
0xffff878690147040 smss.exe                348      4      2        0 ------      0 2020-06-26 15:07:32 UTC+0000                                 
0xffff878690722080 csrss.exe               436    424     10        0      0      0 2020-06-26 15:07:43 UTC+0000                                 
...                ...                     ...    ...    ...      ...    ...    ... ...
0xffff87868ebef080 chrome.exe             2512   5872     21        0      1      0 2020-06-26 15:51:06 UTC+0000                                 
0xffff87868f2e1080 winpmem_v3.3.r         3348    784      5        0      1      1 2020-06-26 15:51:36 UTC+0000                                 
```

... _tadaa_ - looking much better now, aren't we. Since all the process names were fully readable now, it was easy to tell that the memory image was most likely created by `winpmem_v3.3.r` - the process with a PID of _3348_. Therefore, the flag was: `flag{3348}`

**P.S.:** Even though this `winpmem` process was already visible in the upper `pslist`, the newer volatility version will come in handy in the next couple of challenges based on this one.