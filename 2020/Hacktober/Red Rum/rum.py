#!/usr/bin/python3
print(','.join(['RedRum' if not (n%3 or n%5) else 'Red' if not n%3 else 'Rum' if not n%5 else str(n) for n in range(1,501)]))
