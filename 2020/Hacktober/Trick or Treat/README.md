# Trick or Treat

![Programming](https://img.shields.io/badge/Programming--ff8f00?style=for-the-badge) ![Points - 50](https://img.shields.io/badge/Points-50-9cf?style=for-the-badge)

```txt
We found a script being used by DEADFACE. It should be relatively straightforward, but no one here knows Python very well. Can you help us find the flag in this Python file?

file: https://tinyurl.com/yykr7sys
SHA1: 915996d1b858b1be6989f6793f5f9a4282f466d5
Password: hacktober
```

---

As the challenge description already suggests, this is pretty straight-forward to solve.

After you have downloaded and extracted the python file from the URL included in the task statement, simply take a look at the source code: 

```py
from hashlib import md5 as m5


def show_flag():
    b = 'gginmevesogithoooedtatefadwecvhgghu' \
        'idiueewrtsadgxcnvvcxzgkjasywpojjsgq' \
        'uegtnxmzbajdu'
    c = f"{b[10:12]}{b[6:8]}{b[4:6]}{b[8:10]}" \
        f"{b[4:6]}{b[12:14]}{b[2:4]}{b[0:2]}" \
        f"{b[14:16]}{b[18:20]}{b[16:18]}{b[20:22]}"
    m = m5()
    m.update(c.encode('utf-8'))
    d = m.hexdigest()
    return f"flag{{{d}}}"


def show_msg():
    print(f'Smell my feet.')


show_msg()
```

... looks like some fairly regular python code. Where `show_msg` simply prints the text `Smell my feet.` and `show_flag` (which is actually never called by default) would generate and return the flag.

So... let's just add a print statement that will give us the flag, and run the script again:

```py
from hashlib import md5 as m5


def show_flag():
    b = 'gginmevesogithoooedtatefadwecvhgghu' \
        'idiueewrtsadgxcnvvcxzgkjasywpojjsgq' \
        'uegtnxmzbajdu'
    c = f"{b[10:12]}{b[6:8]}{b[4:6]}{b[8:10]}" \
        f"{b[4:6]}{b[12:14]}{b[2:4]}{b[0:2]}" \
        f"{b[14:16]}{b[18:20]}{b[16:18]}{b[20:22]}"
    m = m5()
    m.update(c.encode('utf-8'))
    d = m.hexdigest()
    return f"flag{{{d}}}"


def show_msg():
    print(f'Smell my feet.')


show_msg()
print(show_flag())
```

```bash
python3 ./trickortreat.py
```

... and, _tadaa_, this will give you the flag: `flag{2f3ba6b5fb8bb84c33b584f981c2d13d}`