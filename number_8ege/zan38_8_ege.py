from itertools import *

sp = list(product('АИКЛМЬ', repeat = 6))

for number, elem in enumerate(sp, 1):
    if len(set(elem)) == 6 and elem[0] == 'К' and elem[-1] == 'Ь' and \
    abs(number - (sp.index(elem[::-1]) + 1)) == 26655:
        print(sum(map(int, str(number))))
        break


from itertools import *

count = 0

for elem in product(range(16), repeat = 5):
    if elem[0] != 0 and all(elem.count(i) <= 2 for i in elem) and sum(1 for i in elem if i in (1, 4, 9)) >= 1:
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('ДГИАШЭ', repeat = 5):
    if elem[0] not in 'ИАЭ' and elem[-1] not in 'ДГШ':
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('***+++', repeat = 5):
    if elem[0] != '*' and elem[-1] != '+':
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('0+*+*+*', repeat = 7):
    if elem[0] != '0' and (elem.count('*') + elem.count('0')) == 2:
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('0+*+*+*', repeat = 7):
    elem2 = ''.join(elem).replace('0', '*')
    if elem[0] != '0' and elem2.count('*') == 2:
        count += 1

print(count)

from itertools import *

count = 0

for elem in product('0+*+*+6+*', repeat = 7):
    elem = ''.join(elem)
    elem2 = elem.replace('0', '*').replace('6', '*')
    if elem[0] != '0' and '++' not in elem2 and '**' not in elem2 and elem.count('6') == 1:
        count += 1

print(count)

from itertools import *

s = set()

for elem in permutations('СОРТИРОВКА'):
    elem = ''.join(elem)
    elem2 = elem.replace('Т', 'С').replace('Р', 'С').replace('В', 'С').replace('К', 'С').replace(
        'И', 'А').replace('О', 'А')
    if 'ССС' not in elem2 and 'ААА' not in elem2:
        s.add(elem)

print(len(s))

'''
МАМА

МАМА
МААМ
АММА
ААММ
АМАМ
ММАА

6 сочетаний
1234
МАМА

3214
МАМА

АА - 1 уникальное, permutations - 2, n! = 2! = 2
12
AA: 12, 21

ААА - 1 уникальное, permutations - 6, n = 3 => 3! = 6

123
AAA

123
132
213
231
321
312

АААА - 24 различных перестановки


Две одинаковые буквы -> результат поделить на два (делим на n!)
Три одинаковые буквы -> поделить на 6
'''

from itertools import *

count = 0

for elem in permutations('СОРТИРОВКА'):
    elem = ''.join(elem)
    elem = elem.replace('Т', 'С').replace('Р', 'С').replace('В', 'С').replace('К', 'С').replace(
        'И', 'А').replace('О', 'А')
    if 'ССС' not in elem and 'ААА' not in elem:
        count += 1

print(count // 4)

from itertools import *

count = 0

for elem in permutations('++++++****'):
    elem = ''.join(elem)
    if '+++' not in elem and '***' not in elem:
        count += 1

print(count // 4)

from itertools import *

count = 0

for elem in permutations('+++++*АА'):
    elem = ''.join(elem)
    if 'АА' not in elem:
        count += 1

print(count // 2)