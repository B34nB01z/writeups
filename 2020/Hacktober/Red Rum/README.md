# Red Rum

![Programming](https://img.shields.io/badge/Programming--ff8f00?style=for-the-badge) ![Points - 250](https://img.shields.io/badge/Points-250-9cf?style=for-the-badge)

```txt
We want you to infiltrate DEADFACE as a programmer. Thing is, they're picky about who they bring in. They want to make sure you're the real deal when it comes to programming. Generate a list of numbers 1-500. For each number divisible by 3, replace it with Red; for each number divisible by 5, replace it with Rum. For numbers divisible by both 3 AND 5, replace it with RedRum.

nc env2.hacktober.io 5000
```

---

Ok... I don't think this challenge requires too much explaining - it can be solved quite easily using just a single line of python code ^^:

```py
#!/usr/bin/python3
print(','.join(['RedRum' if not (n%3 or n%5) else 'Red' if not n%3 else 'Rum' if not n%5 else str(n) for n in range(1,501)]))
```

... if you do, however, want a clearer explanation - I've made the code more comprehensible below:

```py
#!/usr/bin/python3

MIN = 1
MAX = 500

for i in range(MIN,MAX+1):
    if i % 3 == 0 and i % 5 == 0:
        print('RedRum', end='')
    elif i % 3 == 0:
        print('Red', end='')
    elif i % 5 == 0:
        print('Rum', end='')
    else:
        print(str(i), end='')
    
    if i < MAX:
        print(',', end='')

print()
```

... anyways... simply pipe this into `netcat` now...

```bash
./rum.py | nc env2.hacktober.io 5000
```

... and retrieve the flag: `flag{h33eeeres_j0hnny!!!}`