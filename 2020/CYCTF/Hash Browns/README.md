# Hash Browns

![Password-cracking](https://img.shields.io/badge/Password%20cracking--780707?style=for-the-badge) ![Points - 400](https://img.shields.io/badge/Points-400-9cf?style=for-the-badge)

```txt
Thanks to your help, we have found evidence relating to the unF0r7un@t3s at the location you uncovered in  in "(un)F0r7un@t3". We apprehended a couple subjects.  It turns out they were planning something bigger, and that was only the beginning.
We found a drive containing password-encrypted, and managed to find the passwords hash, located in hash.txt below.
We have reason to believe that the password starts with the name of a city (in lowercase) in France (which is the country they attacked last), and ends with up to 7 numbers.  For example: paris1337 (don’t try that that’s not the flag).  Please decrypt the password.
- YoshiBoi#2008
```

---

Since it says `name of a city in France` we downloaded [fr.csv](./fr.csv), a file containing the biggest cities of France.  Then we wrote [exploit.py](./exploit.py) to brute force compare hashes with the one from [hash.txt](./hash.txt). 

Result: genoble38100

`CYCTF{grenoble38100}`

