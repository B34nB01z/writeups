# shebang2

![Shebang](https://img.shields.io/badge/Shebang--ff00ff?style=for-the-badge) ![Points - 150](https://img.shields.io/badge/Points-150-9cf?style=for-the-badge)

```txt
This is a bit harder

- stephencurry396#4738
```

---

Once you connect to the server, you'll quickly realize that this is indeed a bit harder ^^. Just look at all those folders:

```bash
ssh shebang2@cyberyoddha.baycyber.net -p1337
/bin/bash
ls
```

```txt
1    11  14  17  2   22  25  28  30  33  36  39  41  44  47  5	 52  55  58  60  63  66  69  71  74  77  8   82  85  88  90  93  96  99
10   12  15  18  20  23  26  29  31  34  37  4	 42  45  48  50  53  56  59  61  64  67  7   72  75  78  80  83  86  89  91  94  97
100  13  16  19  21  24  27  3	 32  35  38  40  43  46  49  51  54  57  6   62  65  68  70  73  76  79  81  84  87  9	 92  95  98
```

... we assumed that somewhere, hidden in the depths of those folders was the flag... so... we used `find` to retrieve it:

```bash
find . -type f -exec grep 'CYCTF' {} \;
```

... _tadaa_ ... there we go: `CYCTF{W0w_th@t$_@_l0t_0f_f1l3s}`
