#!/usr/bin/env python3

from itertools import cycle

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x^y for x, y in zip(a, cycle(b)))

def main():
    with open('output.txt', 'r') as f:
        c: str = f.read()
        e_test: bytes = bytes.fromhex(c.split('\n')[0])
        e_flag: bytes = bytes.fromhex(c.split('\n')[1])
    r_test: bytes = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

    keystream: bytes = xor(e_test, r_test)
    print(f'[+] Recovered flag {xor(e_flag, keystream)} ... ')

if __name__ == '__main__':
    main()
