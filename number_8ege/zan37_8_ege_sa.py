from itertools import *
'''count = 0
for elem in product(sorted('павсикй'), repeat = 6):
    elem = ''.join(elem)
    elem1 = elem.replace('а', '*').replace('и', '*')
    if '**' in elem1:
        count += 1
        if elem == 'какааа':
            print(count)
            break'''
'''for number, elem in enumerate(product(sorted('сублимаця'), repeat=5), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[-1] != 'я' and len([i for i in elem if i in 'уиая']) == 2:
        num = number
print(num)'''

sp = []
for number, elem in enumerate(product('*в*кпрч*', repeat=5), 1): #абвгдеёжзи
    if number % 5 != 0:
        sp.append(elem)
for number, elem in enumerate(sp, 1):
    if '*' not in elem and len(elem) == len(set(elem)):
        print(number)
        break

