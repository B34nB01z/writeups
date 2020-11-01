#!/usr/bin/python3

"""
- Challenge: Bashing My Head
- Summary: Automatically answer questions related to RSA / crypto in general.
- Resources:
    . https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation
    . https://www.cryptool.org/en/cto/highlights/rsa-step-by-step
    . https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
"""

import re
from pwn import *
from base64 import *
from math import gcd
from primePy import primes
from typing import *

def __quick_decrypt_this(r: pwnlib.tubes.remote.remote, rnd: int, v: bytes) -> None:
    """Format should be something like: `Quick, decrypt this: NDIxCg==!`"""
    d = b64decode(v).strip()
    print(f'[*] {v} decrypted is "{d}" ... ')
    r.send(d)

def __is_it_possible_for_p(r: pwnlib.tubes.remote.remote, rnd: int, v: bytes) -> None:
    """Format should be something like: `Supa ez.  Is it possible for p to equal Mjg5Cg==? [y/n]`"""
    p = int(b64decode(v))
    print(f'[*] Got value p={p} ... ')
    k = primes.check(p)
    print(f'[*] Is it possible? {k} ... ')
    yn(r, k)

def __give_me_the_p_and_q(r: pwnlib.tubes.remote.remote, rnd: int, v: bytes) -> None:
    """Format should be something like: `Quick give me the p and q (where p < q) values for when n is NDc5MjEK!`"""
    n = int(b64decode(v))
    p, q = primes.factors(n)
    print(f'[*] Computed prime factors p={p} and q={q} ... ')
    r.send(str(p))
    print(question(r).decode())
    r.send(str(q))

def __is_it_possible_for_n(r: pwnlib.tubes.remote.remote, rnd: int, v: bytes) -> None:
    """Format should be something like: `Now tell me if it is possible for n to equal NDMyNQo=! [y/n]`"""
    n = int(b64decode(v))
    f = primes.factors(n)
    k = len(f) == 2 and f[0] != f[1]
    print(f'[*] Calculated {len(f)} factors: {f} ... ')
    print(f'[*] Is it possible? {k} ... ')
    yn(r, k)

    if k:
        print(f'[*] Calculated factors p={f[0]} and q={f[1]} ... ')
        print(question(r).decode())
        r.send(str(f[0]))
        print(question(r).decode())
        r.send(str(f[1]))

def __tell_me_phi(r: pwnlib.tubes.remote.remote, rnd: int, v: bytes) -> None:
    """Format should be something like: `Tell me ϕ whe n is OTc5OQo=!`"""
    n = int(b64decode(v))
    p, q = primes.factors(n)
    print(f'[*] Calculated factors p={p} and q={q} ... ')
    i = (p-1) * (q-1)
    print(f'[*] Calculated ϕ={i} ... ')
    r.send(str(i))

def __is_it_possible_for_phi(r: pwnlib.tubes.remote.remote, rnd: int, *vs: List[bytes]) -> None:
    """Format should be something like: `Is it possible for ϕ to be MzAxMgo= when e is MjUK? [y/n]`"""
    i, e = int(b64decode(vs[0])), int(b64decode(vs[1]))
    print(f'[*] Got values ϕ={i} and e={e} ... ')
    g = gcd(i, e)
    k = g == 1
    print(f'[*] Calculated gcd={g} ... ')
    print(f'[*] Is it possible? {k} ... ')
    yn(r, k)

QDICT = {
    b'Quick, decrypt this:': __quick_decrypt_this,
    b'Is it possible for p to equal': __is_it_possible_for_p,
    b'give me the p and q': __give_me_the_p_and_q,
    b'possible for n to equal': __is_it_possible_for_n,
    b'Tell me \xcf\x95 whe n is': __tell_me_phi,
    b'Is it possible for \xcf\x95 to': __is_it_possible_for_phi,
}

def yn(r: pwnlib.tubes.remote.remote, b: bool) -> None:
    """Send y/n based on provided boolean `b`"""
    r.send('y' if b else 'n')

def fetch(r: pwnlib.tubes.remote.remote, seq: bytes) -> bytes:
    """Receive until sequence of bytes `seq` has been retrieved."""
    res = b''
    try:
        while not seq in res:
            res += r.recv()
    except EOFError:
        pass
    return res

def question(r: pwnlib.tubes.remote.remote) -> bytes:
    return fetch(r, b'=')

def values(raw: bytes, color: bytes = b'\x1b[34m') -> List[bytes]:
    return list(map(lambda x: x.replace(b'\x1b[0m', b'').replace(color, b''), re.findall(b'\\x1b\[0m.+?'+color.replace(b'\\', b'\\\\').replace(b'[', b'\\['), raw)))

def main():
    r = remote('cyberyoddha.baycyber.net', 10006)
    print(fetch(r, b'---------- Quiz Start ----------').decode())

    try:
        i = 0
        #while True:
        for i in range(60):
            q = question(r)
            if b'=' not in q:
                break
            v = values(q)

            print('\033[0m='*64)
            print(q.decode())
            print('\033[0m='*64)

            found = False
            for p, f in QDICT.items():
                if re.search(p, q):
                    found = True
                    f(r, i, *v)
                    break
            
            if not found:
                print('[-] No matching question signature found ... Exiting ... ')
                break

            i += 1
        print(r.recvall())
    except KeyboardInterrupt:
        print('[*] Interrupted ... Exiting ... ')

if __name__ == '__main__':
    main()
