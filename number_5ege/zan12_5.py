sp = []
for n in range(1, 10 ** 4):
    bin_n = bin(2 * n)[2:]
    sum_n = sum(map(int, bin_n)) #подсчет суммы цифр числа - sum(map(int, str(n)))
    #bin_n.count('1') - сумма цифр двоичной записи
    bin_n += str(sum_n % 2)
    sum_n = sum(map(int, bin_n))
    bin_n += str(sum_n % 2)
    r = int(bin_n, 2)
    if r > 249:
        sp.append(n)
print(min(sp))

import string

def f(number):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % 6]
        number //= 6
    return s[::-1]

sp = []
for n in range(1, 10 ** 4):
    sixth = f(n)
    sum_n = sum(map(int, sixth))
    if sum_n % 5 == 0:
        #sixth = sixth.replace('3', '@').replace('0', '3').replace('@', '0')
        table = str.maketrans('03', '30')
        sixth = sixth.translate(table)
        sixth = '11' + sixth
    else:
        sixth += '44'
        #sixth = sixth[0] + '05' + sixth[3:]
        sixth = sixth.replace(sixth[1], '0', 1).replace(sixth[2], '5', 1)
    r = int(sixth, 6)
    if r > 1500:
        sp.append((n, r))
sp.sort(key = lambda x: (x[1], -x[0]))
print(sp[:10])

sp = []
for n in range(1_000, 10_000):
    numbers = list(map(int, str(n))) #разбитие числа на цифры
    pr = [numbers[0] * numbers[i] for i in range(1, 4)] #список произведений
    pr.sort()
    if ''.join(map(str, pr[1:])) == '5472': #join работает только со строками
        sp.append(n)
print(min(sp))


import math

sp = []
for n in range(10 ** 4, 10 ** 5):
    numbers = list(map(int, str(n)))
    sum_kv = (max(numbers) + min(numbers)) ** 2
    pr = math.prod([i for i in numbers if i % 2 == 0]) #prod() - перемножает все элементы итерируемого объекта
    if ''.join(map(str, sorted([sum_kv, pr], reverse = True))) == '12116':
        sp.append(n)
print(min(sp))


def f2(number):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % 4]
        number //= 4
    return s[::-1]

sp = []
for n in range(1, 10 ** 4):
    fourth = f2(n)
    if len(fourth) % 2 == 0:
        fourth = fourth[:len(fourth) // 2] + '0' + fourth[len(fourth) // 2:]
    r = int(fourth)
    if r <= 180:
        sp.append(n)
print(max(sp))


for n in range(1, 128):
    bin_n = bin(n)[2:].zfill(8) #дополняю незначащами нулями до 8-битной записи
    table = str.maketrans('01', '10')
    bin_n = bin_n.translate(table)
    r = int(bin_n, 2) + 1
    if r == 153:
        print(n)
        break

for n in range(1, 128):
    r = 255 - n + 1 #максимальное 8-битное число - 255
    if r == 153:
        print(n)
        break

def f3(number):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % 5]
        number //= 5
    return s[::-1]

sp = []
for n in range(1, 10 ** 4):
    fifth = f3(n)
    if len(fifth) % 2 != 0:
        fifth += str(n % 5)
    fifth = fifth[len(fifth) // 2:] + fifth[:len(fifth) // 2]
    r = int(fifth, 5)
    if r > 50:
        sp.append(n)
print(min(sp))
        