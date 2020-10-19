from hashlib import md5 as m5


def show_flag():
    b = 'gginmevesogithoooedtatefadwecvhgghu' \
        'idiueewrtsadgxcnvvcxzgkjasywpojjsgq' \
        'uegtnxmzbajdu'
    c = f"{b[10:12]}{b[6:8]}{b[4:6]}{b[8:10]}" \
        f"{b[4:6]}{b[12:14]}{b[2:4]}{b[0:2]}" \
        f"{b[14:16]}{b[18:20]}{b[16:18]}{b[20:22]}"
    m = m5()
    m.update(c.encode('utf-8'))
    d = m.hexdigest()
    return f"flag{{{d}}}"


def show_msg():
    print(f'Smell my feet.')


show_msg()
print(show_flag())
