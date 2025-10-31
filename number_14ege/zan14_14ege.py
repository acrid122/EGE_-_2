for x in range(1, 3001):
    v = 9 ** 150 + 9 ** 30 - x
    count = 0
    while v > 0:
        if v % 9 == 0:
            count += 1
        v //= 9
    if count == 122:
        print(x)
        break

print(int('333332', 4))
print(int('100002', 4))
print(int('FEF', 16))
print(int('1E0', 16))

count = 0
for x in range(int('100002', 4), int('333332', 4) + 1):
    if x % 4 == 2 and x // 16 % 16 == 14:
        count += 1
print(count)

import string 
import math

s = string.digits + string.ascii_uppercase

sp = [] #список для A
for x in s[:15]:
    M = int(f'432{x}3', 15)
    N = int(f'86{x}86', 15)
    res = math.ceil(M / N)
    M1 = res * N
    A = M1 - M
    sp.append(A)
print(min(sp))

print(int('1C28', 16))
print(7208 % 16)


import string
s = string.digits + string.ascii_uppercase

s1 = {1} #множество - неупорядоченная коллекция уникальных элементов (в множестве не хранятся дубликаты)
for x in s[1:25]:
    ch1 = int(f'8AF7{x}11', 25)
    ch2 = int(f'{x}DA87', 25)
    r = ch1 + ch2
    for y in range(1, 101):
        if r % y == 0:
            s1.add(y) #метод .add() - добавление в множество
print(len(s1))


#множество внутри себя может хранить только хэшируемые объекты (но для простоты возьмем неизменяемые)

print(int('6666666', 7))
def f5(n):
    sd = string.digits
    s = ""
    while n:
        s += sd[n % 5]
        n //= 5
    return s[::-1]

count = 0
for x in range(15, int('6666666', 7) + 1, 16):
    fifth = f5(x)
    if sum([fifth.count(i) % 2 for i in set(fifth)]) <= 1:
        count += 1
print(count)