import string

for x in string.printable[18::-1]:
    ch1 = int(f"2e{x}g8", 19)
    ch2 = int(f"6f{x}bg", 19)
    s = ch1 + ch2
    if s % 18 == 0:
        print(s // 9)
        break


def f(x, a):
    return sum(x[i] * a ** (len(x) - i - 1) for i in range(len(x)))

for x in range(40):
    ch1 = f([8, 7, 1, x, 2, 9, 1], 40)
    ch2 = f([3, 6, 6, x, 6, 3, 1], 40)
    ch3 = f([9, 7, 3, x, 6, 1, 8], 40)
    s = ch1 + ch2 + ch3
    if s % 39 == 0:
        print(s // 13)
        break

def f1(x, a):
    return sum(x[i] * a ** i for i in range(len(x)))

for x in range(40):
    ch1 = f1([8, 7, 1, x, 2, 9, 1][::-1], 40)
    ch2 = f1([3, 6, 6, x, 6, 3, 1][::-1], 40)
    ch3 = f1([9, 7, 3, x, 6, 1, 8][::-1], 40)
    s = ch1 + ch2 + ch3
    if s % 39 == 0:
        print(s // 13)
        break

""" mas = []
for x in range(1, 32000 + 1):
    v = 75 ** 314 + 75 ** 118 - x
    count = 0
    while v > 0:
        if v % 75 == 0:
            count += 1
        v //= 75
    mas.append(count)

print(min(mas))

import string

s = string.printable[:21]

for x in s:
    for y in s:
        ch1 = int(f"12{y}{x}9", 21)
        ch2 = int(f"36{y}99", 21)
        summa = ch1 + ch2
        if summa % 18 == 0:
            ch1 = int(f"125{x}9", 21)
            ch2 = int(f"36599", 21)
            print((ch1 + ch2) // 18)
            exit() """

v = (16 ** 350 * (15 * 3 - 29) ** 16384 + 1007) // 63

'''
Exception has occurred: OverflowError
integer division result too large for a float
    v = (16 ** 350 * (15 * 3 - 29) ** 16384 + 1007) / 63
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~
OverflowError: integer division result too large for a float
'''

count = 0
while v > 0:
    if v % 4 == 1: count += 1
    v //= 4
print(count)



#print(Fraction((16 ** 350 * (15 * 3 - 29) ** 16384 + 1007), 63))

from fractions import Fraction

v = Fraction((16 ** 350 * (15 * 3 - 29) ** 16384 + 1007), 63)

count = 0
while v > 0:
    if v % 4 == 1: count += 1
    v //= 4
print(count)

'''
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
'''