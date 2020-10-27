# Firmware update

![Reversing](https://img.shields.io/badge/Reversing--ff6100?style=for-the-badge) ![Points - 500](https://img.shields.io/badge/Points-500-9cf?style=for-the-badge)

```txt
The crypto software LibrePLC at BB Industry is continuously receiving updates. Unfortunately, the responsible employee left the company a few weeks ago and hasn't deployed the most recent firmware with important security updates. He just left a note with 5157CA3SDGF463249FBF.

We urgently need the new firmware!
```

---

First, simply open the first zip archive `LibrePLC_fw_1.0.0.zip` using the weird string from the task description: `5157CA3SDGF463249FBF`.

This will give you two new files: `key` and `LibrePLC_fw_1.0.0.bin`. As a quick `file` command will tell you, the first one is actually a Python script. So... let's have a look!

```py
#!/usr/bin python3
import hashlib #line:3
import sys #line:4
def check ():
        if len (sys .argv )==1 :#
                print ("No key for you")#
                sys .exit (0 )#line:9
        else :#line:10
                OOO0OOOOOO00000OO =sys .argv [1 ]#
                return OOO0OOOOOO00000OO #line:12
def get_it (OOO0OOOOO00000OOO ):#line:14
        with open (OOO0OOOOO00000OOO ,"rb")as O0000O000O00O0000 :#line:15
                O0O0O0OOO000OOO0O =O0000O000O00O0000 .read ()
                OO0O000O0OO000O0O =hashlib .sha256 (O0O0O0OOO000OOO0O ).hexdigest ()
        return OO0O000O0OO000O0O #line:18
def keys (OOOOOOOO00OOOOOOO ):#line:20
        O0OO00OOO00OOOOOO =OOOOOOOO00OOOOOOO [::-1 ][:10 ]#line:21
        O00O00O0O0O0O0000 =OOOOOOOO00OOOOOOO [5 :20 ][::-1 ]#line:22
        O00O00O0O0O0O0000 =O0OO00OOO00OOOOOO .replace ("1","0")[::-1 ].replace ("9","sys")#
        O0OO00OOO00OOOOOO =O00O00O0O0O0O0000 .replace ("a","k").replace ("4","q").replace ("b","c").replace ("5","kron")#line:24
        O0O000OO0000O000O =OOOOOOOO00OOOOOOO [23 :50 ][::-1 ].replace ("8","n")
        O0OO0OO0OOOOO0OO0 =OOOOOOOO00OOOOOOO [50 :61 ][::-1 ].replace ("7","ctf")#
        O0OO00O00000O00O0 =(O00O00O0O0O0O0000 +O0OO0OO0OOOOO0OO0 +O0OO00OOO00OOOOOO +O0O000OO0000O000O ).upper ()#
        return O0OO00O00000O00O0 #line:30
print (keys (get_it (check ())))
```

... well... we can already kind of see what is happening... still... it doesn't look to nice... Let's clean it up first!

```py
#!/usr/bin python3

import hashlib
import sys

def check():
    if len (sys.argv) == 1:
        print("No key for you")
        sys.exit(0)
    else:
        return sys.argv[1]

def get_it(p):
    with open(p, "rb") as f:
        content = f.read()
        hash = hashlib.sha256(content).hexdigest()
    return hash

def keys(p):
    a = p[::-1][:10]
    b = p[5:20][::-1]
    b = a.replace("1","0")[::-1].replace("9","sys")
    a = b.replace("a","k").replace("4","q").replace("b","c").replace("5","kron")
    c = p[23:50][::-1].replace("8","n")
    d = p[50:61][::-1].replace("7","ctf")
    res = (b + d + a + c).upper()
    return res

print(keys(get_it(check())))
```

... that's much better! We can now clearly see what this script is doing:

1. it takes a filename as a command line argument.
2. ... then it computes the sha256 hash of the file's contents ...
3. and last but not least, some replacing and weird stuff is happening, only for the result to be returned and printed.

... _hmm_ ... what file could we possibly need in order to retrieve a proper value from this `keys()` function ... let's try the weird _.bin_ file that was also part of the first zip archive ...

```txt
$ ./key.py LibrePLC_fw_1.0.0.bin
7SYSCC3076BDCTF13CC9CTFA6CB7SYSCC3076CD56579549EC5AB533EN03AFC1F9N
```

... this couldn't, by any chance be the password to the next zip archive, could it? ... it is! Repeat this with the _bin_ file in the second zip archive until you have extracted the contents of the last archive `LibrePLC_fw_1.0.2.zip`.

The flag is actually just in this last binary file, as `strings` will tell you. _Tadaa_, you've successfully retrieved the flag: `syskronCTF{s3Cur3_uPd4T3}`
