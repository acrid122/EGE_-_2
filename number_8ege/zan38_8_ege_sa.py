from itertools import *

'''count = 0

for elem in product('взгляд', repeat = 4):
    if sum(1 for i in elem if i == 'з') == 1 or sum(1 for i in elem if i == 'з') == 2:
        count += 1
print(count)'''

'''count = 0

for elem in permutations('м*р*н*'):
    if elem[0] != '*':
        count += 1
print(count // 2)'''

'''count = 0

for elem in product('0+*+*+*', repeat=5):
    elem2 = ''.join(elem).replace('0', '*')
    if elem[0] != '0':
        if '***' not in elem2 and elem2.count('**') >= 2:
            count += 1
print(count)'''

'''count = 0

for elem in product(range(25), repeat=4):
    if elem[0] != 0:
        if sum(1 for i in elem if i <= 5) <= 2 and sum(1 for i in elem if i % 2 != 0) == 1:
            count += 1
print(count)'''

'''count = 0

for elem in product('0+*+*5*+*+*+*', repeat=6):
    elem2 = ''.join(elem).replace('0', '*').replace('5', '+')
    if elem[0] != '0':
        if elem.count('5') <= 1 and '++' not in elem2:
            count += 1
print(count)'''

count = 0

for elem in product(range(7), repeat=5):
    if elem[0] != 0:
        sum_ch = sum(i for i in elem if i % 2 == 0)
        sum_nch = sum(i for i in elem if i % 2 != 0)
        if elem.count(6) == 1 and sum_ch < sum_nch:
            count += 1
print(count)


