# shebang3

![Shebang](https://img.shields.io/badge/Shebang--ff00ff?style=for-the-badge) ![Points - 150](https://img.shields.io/badge/Points-150-9cf?style=for-the-badge)

```txt
These files are the same...

- stephencurry396#4738
```

---

The description actually tells you pretty much exactly what to do: find the difference ^^.

You can just use the UNIX `diff` command to do that for you:

```bash
diff file.txt file2.txt
```

```txt
106526a106527
> C
107719a107721
> Y
108477a108480
> C
109644a109648
> T
109873a109878
> F
110293a110299
> {
111434a111441
> S
111715a111723
> P
111969a111978
> O
112285a112295
> T
112548a112559
> _
113046a113058
> T
113525a113538
> H
114286a114300
> 3
114773a114788
> _
115594a115610
> D
116750a116767
> 1
117691a117709
> F
118643a118662
> F
121288a121308
> }
...
```

... _et voilà_ ... the flag was: `CYCTF{SPOT_TH3_D1FF}`
