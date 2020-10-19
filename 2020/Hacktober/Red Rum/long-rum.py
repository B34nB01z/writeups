#!/usr/bin/python3

MIN = 1
MAX = 500

for i in range(MIN,MAX+1):
    if i % 3 == 0 and i % 5 == 0:
        print('RedRum', end='')
    elif i % 3 == 0:
        print('Red', end='')
    elif i % 5 == 0:
        print('Rum', end='')
    else:
        print(str(i), end='')

    if i < MAX:
        print(',', end='')

print()
