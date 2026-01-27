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


from itertools import *
num = 0
for number, elem in enumerate(product(sorted("СУБЛИМАЦЯ"), repeat = 5), 1):
    elem = ''.join(elem)
    if number % 2 != 0 and elem[-1] != 'Я' and sum(1 for i in elem if i in "УИАЯ") == 2:
        num = number
print(num)


from itertools import *
sp = []
for n, e in enumerate(product("*В*КПРЧ*", repeat = 5), 1):
    if n % 5 != 0:
        sp.append(e)
for n, e in enumerate(sp, 1):
    e = ''.join(e)
    if len(set(e)) == len(e) and e.count('*') == 0:
        print(n)
        break