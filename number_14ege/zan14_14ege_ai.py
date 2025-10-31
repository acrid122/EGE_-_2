for x in range(3000, 0, -1):
    s = 9 * 11 ** 210 + 8 *  11 ** 150 - x
    count = 0
    while s > 0:
        if s % 11 == 0:
            count += 1
        s //= 11
    if count == 60:
        print(x)
        break

for x in range(2400, 0, -1):
    s = 7 * 9 ** 210 + 6 * 9 ** 110 - x
    count = 0
    while s > 0:
        if s % 9 == 0:
            count += 1
        s //= 9
    if count == 100:
        print(x)
        break


grn = max([int('1300220', 4), int('10050', 8), int('1C28', 16)])
grv = min([int('1333223', 4), int('17750', 8), int('FC28', 16)])
for x in range(grn, grv + 1):
    if (x % 16 == 8) * (x // 16 % 16 == 2) * (x // 16**2 % 16 == 12) * (x % 8 == 0) \
        * (x // 8 % 8 == 5) * (x // 8 ** 4 % 8 == 1) * (x // 4 % 4 == 2) \
        * (x // 4 ** 2 % 4 == 2) * (x // 4 ** 5 % 4 == 3) * (x // 4 ** 6 % 4 == 1):
        print(x)

s = set()
for x in range(10, 67):
    for y in range(0, x):
        ch1 = y * 67 + 67  + x * 67 ** 2 + 3 * 67 ** 3 + 7 * 67 ** 4
        ch2 = 6 + y * 67  + 9 * 67 ** 2 + 4 * 67 ** 3
        v = ch1 + ch2
        s.add(v)
print(len(s))

