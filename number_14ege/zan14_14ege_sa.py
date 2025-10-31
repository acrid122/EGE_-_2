for x in range(3000, 0, -1):
    count = 0
    v = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    while v > 0:
        if v % 11 == 0:
            count += 1
        v //= 11
    if count == 60:
        print(x)
        break

for x in range(2400, 0, -1):
    v = 7 * 9 ** 210 + 6 * 9 ** 110 - x
    count = 0
    while v > 0:
        if v % 9 == 0:
            count += 1
        v //= 9
    if count == 100:
        print(x)
        break
    
grn = max([int('1300220', 4), int('10050', 8), int('1C28', 16)])
grv = min([int('1333223', 4), int('17750', 8), int('FC28', 16)])
for x in range(grn, grv + 1):
    if (x % 16 == 8) and (x // 16 % 16 == 2) and (x // 16 // 16 % 16 == 12) and \
        (x % 8 == 0) and (x // 8 % 8 == 5) and (x // (8 ** 4) % 8 == 1) and \
            (x // 4 % 4 == 2) and (x // (4 ** 2) % 4 == 2) and \
                (x // (4 ** 5) % 4 == 3) and (x // (4 ** 6) % 4 == 1):
        print(x)

import string 
s = string.digits + string.ascii_uppercase
for x in s[1:25]:
    count = 0
    for y in range(1, 101):
        ch1 = int(f'8AF7{x}11', 25)
        ch2 = int(f'{x}DA87', 25)
        v = ch1 + ch2
        if v % 9 == 0:
            count += 1
    
s = set()
for x in range(10, 67):
    for y in range(x):
        ch1 = 7 * 67 ** 4 + 3 * 67 ** 3 + x * 67 ** 2 + 67 + y
        ch2 = 4 * x ** 3 + 9 * x ** 2 + y * 67 + 6
        s.add(ch1 + ch2)
print(len(s))

def f(num, base):
    s = string.digits + string.ascii_uppercase
    s1 = ''
    
