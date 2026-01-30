from itertools import *
s = set()
for elem in product(sorted('ВЗЛГЯД'), repeat = 4):
    elem = ''.join(elem)
    if 1 <= elem.count('З') <= 2:
        s.add(elem)
print(len(s))

from itertools import *
count = 0
for elem in permutations("МАРИНА"):
    elem = ''.join(elem)
    if elem[0] not in 'АИ':
        count += 1
print(count // 2)

from itertools import *
count = 0
for elem in product('0121212', repeat = 5):
    elem = ''.join(elem)
    s = elem.replace('0', '2')
    if elem[0] != '0' and s.count('22') >= 2 and '222' not in s:
        count += 1
print(count)


from itertools import *
count = 0
for elem in product(range(25), repeat=4):
    if elem[0] != 0 and sum(1 for i in elem if i % 2 != 0) == 1 and sum(1 for i in elem if i <= 5) <= 2:
        count += 1
print(count)

from itertools import *
count = 0
for elem in product('0*+*+5+*+*+*+', repeat=6):
    elem = ''.join(elem)
    s = elem.replace('5', '*')
    if elem[0] != '0' and sum(1 for i in elem if i == '5') <= 1 and '**' not in s:
        count += 1
print(count)


from itertools import *
count = 0
for elem in product('0123456', repeat = 5):
    elem = ''.join(elem)
    if elem[0] != '0' and elem.count('6') == 1 and sum(int(i) for i in elem if int(i) % 2 == 0) < sum(int(i) for i in elem if int(i) % 2 != 0):
        count += 1
print(count)