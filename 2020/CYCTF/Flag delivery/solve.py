#!/usr/bin/python3

msg = ''
with open('flag.txt', 'r') as f:
    msg = f.read()

print(msg.replace('?M6', '.').replace('D', '-'))
