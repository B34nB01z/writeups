#!/usr/bin/env python3

from itertools import cycle

def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x^y for x, y in zip(a,cycle(b))])

def main():
    with open('output.txt', 'r') as f:
        lines: List[bytes] = [bytes.fromhex(l) for l in f.read().split('\n') if l]
    for i, l in enumerate(lines):
        print(f'\r[*] Trying #{i:02x} ... ')
        x: bytes = xor(l[:len('CHTB{')], b'CHTB{')
        if x[0] == x[1] == x[2] == x[3] == x[4]:
            with open('cracked.txt', 'wb') as f:
                f.write(xor(l, bytes([x[0],])))
            print(f'[+] Found flag in line #{i:02x}; key = 0x{x[0]:02x} ... ')
            break

if __name__ == '__main__':
    main()
