v = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
a = set()
while v > 0:
    if (v % 17) % 2 == 0:
        a.add(v % 17)
    v //= 17
print(len(a))

for x in range(2006, 0, -1):
    v = 4 ** 163 * 5 + 12 ** 62 - x
    count_1, count_4 = 0, 0
    while v > 0:
        if v % 5 == 1:
            count_1 += 1
        if v % 5 == 4:
            count_4 += 1
        v //= 5
    if count_1 < count_4:
        print(x)
        break
    
    
sp = []
for x in range(2, 2026):
    v = 5 ** 2025 + 5 ** 200 - x
    count = 0
    while v > 0:
        if v % 5 == 4:
            count += 1
        v //= 5
    sp.append([x, count])
    #sp.append([count, x])
sp.sort(key = lambda x: (-x[1], -x[0]))
#sp.sort(reverse = True)
print(sp[0][0])
#print(sp[0][1])


""" for p in range(7, 10 ** 5):
    for x in range(1, p):
        for y in range(1, p):
            for z in range(p):
                ch1 = y * p ** 2 + 4 * p + y
                ch2 = y * p ** 2 + 6 * p + 5
                ch3 = x * p ** 3 + z * p ** 2 + 3 * p + 3
                if ch1 + ch2 == ch3:
                    v = x * p ** 2 + y * p + z
                    print(v)
                    exit() """
def f(x, a):
    return sum(x[i] * a ** (len(x) - i - 1) for i in range(len(x)))

for x in range(66, -1, -1):
    ch1 = f([3, x, 2, 1], 81)
    ch2 = f([1, 7, x, 4], 67)
    if (ch1 + ch2) % 35 == 0:
        print((ch1 + ch2) // 35)
        break


for x in range(97, -1, -1):
    ch1 = f([1, 2, x, 4, 5], 98)
    ch2 = f([1, x, 9, 8], 123)
    if (ch1 + ch2 ) % 123 == 0:
        print((ch1 + ch2 ) // 123)
        break

for x in range(67, -1, -1):
    ch1 = f([1, 2, 3, x, 5], 68)
    ch2 = f([1, x, 2, 3, 3], 68)
    if (ch1 + ch2) % 12 == 0:
        print((ch1 + ch2) // 12)
        break

import string

def p(x):
    x = x.lower()
    return string.printable.index(x)


def f(x, a):
    return sum(x[i] * a ** (len(x) - i - 1) for i in range(len(x)))

""" def f(x, a):
    return sum(elem * a ** j for elem, j in enumerate(x[::-1])) """

for x in range(10):
    ch1 = f(list(map(p, 'SLADOST')), 36)
    ch2 = f(list(map(p, 'GADOST')), int(f'10{x}'))
    ch3 = f(list(map(p, 'HALLOWEEN')), 50 - x)
    ch4 = 166729861760449
    if ch1 + ch2 == ch3 - ch4:
        print(f(list(map(p, 'GADOST')), int(f'{x}13')))
        break    
    
sp = []
for x in range(10, 14):
    for y in range(9, x):
        ch1 = f([7, x, 3, 7, y], 14)
        ch2 = f([9, y, 6, 3], x)
        ch3 = f([1, 5, 1, 4, 8], y)
        v = ch1 + ch2 - ch3
        sp.append([v, v // (x + y)])
sp.sort(key = lambda x: -x[0])
print(sp[0][1])