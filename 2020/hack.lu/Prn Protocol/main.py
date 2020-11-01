#!/usr/bin/python3

import struct
from pwn import *
from typing import *

types = {
    'message_id': 0x1,
    'identifier': 0x2,
    'member_id':  0x3,
    'login':      0x4,
    'flag':       0x5,
    'error':      0xff,
}

errors = {
    0x01: 'Recieved to many bytes only 32 bytes in total are allowed.',
    0x02: 'Recieved a payload with length < 2. Or very large size.',
    0x03: 'Calculated payload length differs from recieved payload length.',
    0x04: 'Recieved unknown payload type.',
    0x05: 'Recieved less than three payloads.',
    0x06: 'First payload is not Message ID.',
    0x07: 'Second payload is not Identifier.',
    0x08: 'Found a payload type a second time.',
    0x09: 'Recieved to many messages in this session.',
    0x10: 'Did not expect payload.',
    0x11: 'Recieved invalid message ID.',
    0x20: 'Did not expect payload.',
    0x21: 'Recieved invalid identifier.',
    0x30: 'Did not expect payload.',
    0x31: 'Client used server code 0x01.',
    0x32: 'Client used server code 0x03.',
    0x33: 'Client used server code 0x04.',
    0x34: 'Unknown code from client.',
    0x40: 'Did not expect payload.',
    0x41: 'Username is to short/long.',
    0x42: 'Password is to short/long.',
    0x43: 'Recieved invalid username.',
    0x44: 'Recieved invalid password.',
    0x45: 'Client send login without knowing the credentials.',
    0x46: 'Client is already logged in.',
    0x47: 'Unknown code from client.',
    0x50: 'No Flag at this point.',
}


class PrnPacket(object):
    def __init__(self, ptype: int, data: bytes, check: bool = True):
        if check and len(data)+1 > 32:
            raise Exception('Too much data!')
        self.plen: int = len(data)+1
        self.ptype: int = ptype
        self.data: int = data

    def raw(self) -> bytes:
        return bytes([self.plen, self.ptype]) + self.data

    def __str__(self) -> str:
        return f'PrnPacket{{ len={self.plen:x}, type={self.ptype:x}, data={self.data} }}'

    @classmethod
    def parse(cls, raw: bytes) -> "PrnPacket":
        p = PrnPacket(raw[1], raw[2:])
        if p.plen != raw[0]:
            raise Exception('Length mismatch!')
        return p

    @classmethod
    def parse_all(cls, raw: bytes) -> List["PrnPacket"]:
        i = 0
        ps = []
        while i < len(raw):
            if raw[i] == 0:
                break
            ps.append(PrnPacket(raw[i+1], raw[i+2:i+1+raw[i]], check=False))
            i += raw[i]+1
        return ps

class PrnError(Exception):
    def __init__(self, code: int):
        self.code = code

    def msg(self) -> str:
        return errors[self.code]

    def __str__(self) -> str:
        return f'PrnError{{ code={self.code}, msg="{self.msg()}" }}'

class PrnSession(object):
    def __init__(self, r: pwnlib.tubes.remote.remote):
        self.r: pwnlib.tubes.remote.remote = r
        self.msg_id: int = -1
        self.prn_id: bytes = b''

        self.uname: str = ''
        self.pwd: str = ''

    def init(self) -> None:
        ps = PrnPacket.parse_all(self.r.recv())
        self.msg_id: int = ps[0].data[0]
        self.prn_id: bytes = ps[1].data

    def __headers(self) -> bytes:
        h = PrnPacket(ptype=types['message_id'],data=bytes([self.msg_id])).raw() +\
            PrnPacket(ptype=types['identifier'],data=self.prn_id).raw()
        return h

    def __update_headers(self, packets: Tuple[PrnPacket, PrnPacket]) -> None:
        self.msg_id = packets[0].data[0]
        self.prn_id = packets[1].data

    def __check_res(self, packets: List[PrnPacket]) -> None:
        if packets[0].ptype == types['error']:
            raise PrnError(packets[0].data[0])
        self.__update_headers((packets[0],packets[1]))

    def req_member_id(self) -> Tuple[str, str]:
        self.r.send(self.__headers() + PrnPacket(ptype=types['member_id'],data=b'\x02').raw())
        ps = PrnPacket.parse_all(self.r.recv())
        self.__check_res(ps)
        self.uname = ps[2].data[1:].decode()
        self.pwd = ps[3].data[1:].decode()
        return (self.uname, self.pwd)

    def login(self) -> bool:
        self.r.send(self.__headers() + PrnPacket(ptype=types['login'],data=b'\x01').raw())
        #print(f'[*] Received: {self.r.recv()}')
        self.r.recv()
        self.r.sendline(self.uname.encode())
        #print(f'[*] Received: {self.r.recv()}')
        self.r.recv()
        self.r.sendline(self.pwd.encode())
        ps = PrnPacket.parse_all(self.r.recv())
        self.__check_res(ps)
        return ps[2].data[0] == 0x2

    def flag(self) -> string:
        self.r.send(self.__headers() + PrnPacket(ptype=types['flag'],data=b'\x01').raw())
        ps = PrnPacket.parse_all(self.r.recv())
        self.__check_res(ps)
        return ps[2].data.decode()

    def __str__(self) -> str:
        return f'PrnSession{{ r={self.r}, msg_id={self.msg_id}, prn_id={self.prn_id} }}'

def main():
    r = remote('flu.xxx', 2005)
    s = PrnSession(r)
    s.init()

    i = 0
    while i < 3:
        inp = input(f'[{i:d}]: ').strip()

        try:
            if inp == 'exit':
                break
            elif inp == 'req member id':
                uname, pwd = s.req_member_id()
                print(f'[+] Received username="{uname}" password="{pwd}" ... ')
            elif inp == 'login':
                if s.login():
                    print('[+] Successfully logged in!')
                else:
                    print('[-] Couldn\'t log in!')
            elif inp == 'flag':
                print(f'[+] Received flag: "{s.flag()}"')
            elif inp == 'help':
                print('Welcome to uselessTerm!')
                print('This terminal is essentially useless, you simply need to enter the following commands in the given order: ')
                print('\t$ req member id')
                print('\t$ login')
                print('\t$ flag')
                print('Thank you for choosing uselessTerm!')
                continue
            else:
                print('[-] Unknown command!')
                continue
        except PrnError as e:
            print(f'[-] {e}')
            continue

        i += 1

if __name__ == '__main__':
    main()
