#!/usr/bin/env python3

import re
from pwn import *
from typing import *

def sub(s: str,  mapping: Dict[str, Any]) -> str:
    for k, v in mapping.items():
        s = s.replace(k, str(v))
    return s

def main():
    r = remote('138.68.133.178', 31654)

    r.recvuntil('> ')
    r.sendline('1')
    r.recvuntil('help:\n\n')

    res: List[str] = re.sub(r'\s+', ' ', r.recvuntil('\n').decode().strip().replace('->', '')).split(' ')
    mapping: Dict[str, int] = { res[i]: int(res[i+1]) for i in range(0, len(res), 2) }

    r.recvuntil('> ')
    r.sendline('2')

    for i in range(500):
        r.recvuntil(':\n\n')
        task: str = r.recvuntil('\n\n').decode().strip()
        x: int = eval(sub(task[:task.index('=')], mapping))
        print(f'[*] Round #{i:03d}: x = {x} ... ')
        r.sendafter('Answer: ', str(x)+'\n')

    r.interactive()

if __name__ == '__main__':
    main()
