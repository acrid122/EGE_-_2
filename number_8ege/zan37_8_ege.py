from itertools import *

'''
product() - генерация всех возможных сочетаний с повторениями, где порядок элементов
важен. декартово произведение.
'''

print(list(product('ABCD', repeat = 2)))

'''
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), 
('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), 
('C', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C'), 
('D', 'D')]
'''

'''
permutations() - генерация всех возможных перестановок (сочетания без повторений),
где порядок элементов важен.
'''

print(list(permutations('ABCD', r = 2)))

'''
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'),
 ('B', 'D'), ('C', 'A'), 
('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
'''

'''
combintations() - генерация всех возможных комбинаций, где нет повторений
и порядок элементов не важен
'''

print(list(combinations('ABCD', r = 2)))

'''
[('A', 'B'), ('A', 'C'), ('A', 'D'),
 ('B', 'C'), ('B', 'D'), ('C', 'D')]
'''

#enumerate

a = [5, 6, 7, 8]

print(list(enumerate(a, 1)))

from itertools import *

for number, elem in enumerate(product(sorted('ГРАНИТ'), repeat = 6), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[0] not in 'АИГ' and elem.count('А') == 1:
        print(number)
        break

from itertools import *

summa = 0

for number, elem in enumerate(product(sorted('ТВОРИЛКА'), repeat = 6), 1):
    elem = ''.join(elem)
    if elem == 'ВИКТОР' or elem == 'КИРИЛЛ':
        summa += number

print(summa)

from itertools import * 

for number, elem in enumerate(product(sorted('КОДИМ'), repeat = 5), 1):
    elem = ''.join(elem)
    if elem.count('М') == 2 and 'ММ' not in elem:
        num = number

print(num)

from itertools import * 

count = 0

for number, elem in enumerate(product(sorted('ПРЕСТОЛ'), repeat = 5), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[-1] in 'ЕО' and sum(elem.count(i) for i in 'ПРСТЛ') <= 3:
        count += 1

print(count)

from itertools import * 

count = 0

for number, elem in enumerate(product('*****++', repeat = 5), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[-1] == '+' and elem.count('*') <= 3:
        count += 1

print(count)

from itertools import * 

sp = []

for number, elem in enumerate(product(sorted('КОФЕ'), repeat = 5), 1):
    elem = ''.join(elem)
    elem = elem.replace('Ф', 'К') #replace(), чтобы привести к одной букве
    if elem.count('О') == 1 and 'ОК' not in elem and 'КО' not in elem:
        sp.append(number)

print(sp[0] + sp[-1])

from itertools import * 

sp = []

for number, elem in enumerate(product(sorted('КОФЕ'), repeat = 5), 1):
    elem = ''.join(elem)
    table = str.maketrans('Ф', 'К')
    elem = elem.translate(table)
    if elem.count('О') == 1 and 'ОК' not in elem and 'КО' not in elem:
        sp.append(number)

print(sp[0] + sp[-1])

from itertools import * 

sp = []

for number, elem in enumerate(product('Е*О*', repeat = 5), 1):
    elem = ''.join(elem)
    if elem.count('О') == 1 and 'О*' not in elem and '*О' not in elem:
        sp.append(number)

print(sp[0] + sp[-1])

from itertools import * 

for number, elem in enumerate(product('Д*ЙПНТЬ*', repeat = 4), 1):
    elem = ''.join(elem)
    if '*' not in elem and len(elem) == len(set(elem)):
        num = number

print(num)

from itertools import * 

count = 0

for elem in product('012345678', repeat = 6):
    if elem[0] != '0':
        count += 1
        elem = ''.join(elem)
        elem2 = elem.replace('3', '1').replace('5', '1').replace('7', '1')
        if '11' not in elem2 and count % 10 == 5:
            elem1 = elem

print(elem1)

from itertools import *

count = 0

for elem in product(sorted('ПАВСКИЙ'), repeat = 6):
    elem = ''.join(elem)
    elem2 = elem.replace('А', 'И')
    if 'ИИ' in elem2:
        count += 1
        if elem == 'КАКААА':
            print(count)
            break