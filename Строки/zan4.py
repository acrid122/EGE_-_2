s = 'Hello, world'
s1 = s.upper()
s2 = s1.center(20)
print(s2)

v = 'Hello, World'
print(v.upper().center(20)) #если хочется применить несколько методов сразу

#Поиск замена

#10. .count(sub, start = 0, end = len(s)). Считает количество подстрок sub в строке. Если передаем позиции, то передаем индексы. Регистрозависим.

print(v.count('l'))
print(v.count('l', 3)) #передаю позицию старта
print(v.count('l', 2, 8)) #только end передать нельзя.

print(v.count('o'))
print(v.count('o', 4))

#11. .find(sub, start = 0, end = len(s)). Индекс первого вхождения слева. Если передаем позиции, то передаем индексы. end - невключительно.

print(v.find('l'))
print(v.find('l', v.find('l') + 1))
print(v.find('l', v.find('l', v.find('l') + 1) + 1))
print(v.find('b')) #если подстроки в строке нет, то выводится -1

#12. .index(sub, start = 0, end = len(s)). Индекс первого вхождения слева. Если передаем позиции, то передаем индексы.

'''
Тот же самый функционал, что и у .find(), но отличается тем, что при поиске подстроки, которой нет в строке, он выдает ошибку ValueError.
'''

try:
    print(v.index('b'))
except ValueError:
    print('Такого символа в строке нет')

#13. .rfind(sub, start = 0, end = len(s)). Индекс первого вхождения справа (последнего слева). Если передаем позиции, то передаем индексы.

print(v.rfind('l'))

#14. .rindex(sub, start = 0, end = len(s)). Индекс первого вхождения справа (последнего слева). Если передаем позиции, то передаем индексы.

'''
Тот же самый функционал, что и у .rfind(), но отличается тем, что при поиске подстроки, которой нет в строке, он выдает ошибку ValueError.
'''

#15. .replace(old, new, count = -1). Заменить подстроку в строке. Третий параметр - количество вхождений слева, которые надо заменить.
#По умолчанию меняет все.

print(v.replace('l', 'd'))
print(v.replace('l', 'd', 2))
print(v.lower().replace('l', 'd', 1))
print(v.swapcase().rjust(30).replace('D', 'e'))

#16. .translate(table) / str.maketrans(). .maketrans() - метод класса str, который делает таблицу перевода. 
# .translate(table) - метод, который применяет данную таблицу к строке. Не сможет заменить подстроку из нескольких символов.

print(v.replace('l', '1').replace('e', '2').replace('d', '3'))

table = str.maketrans('led', '123') #такой способ работает так: l -> 1, e -> 2, d -> 3
print(v.translate(table))

table1 = str.maketrans({
    'l' : '1',
    'e' : '2',
    'd' : '3'
})

print(v.translate(table1))

table2 = str.maketrans('led', '123', 'ow')
print(v.translate(table2))

print(v.replace('l', '')) #замена на пустую строку равносильна удалению
table3 = str.maketrans('od', '89', 'l')
print(v.translate(table3))
table4 = str.maketrans('l', '7', 'o')
print(v.translate(table4))

#Проверка префиксов / суффиксов

#17. .startswith(prefix, start = 0, end = len(s)). Начинается ли строка с prefix

print(v.startswith('Hello'))
print(v.startswith('world', 7))

#18. .endswith(suffix, start = 0, end = len(s)). Заканчивается ли строка suffix

print(v.endswith('world'))
print(v.endswith('wor', 7, 10))

#Разделение и объеединение

#19. .split(sep = None, maxsplit = -1). По умолчанию делит по пробелу. Разделяет строку по sep на maxsplit + 1 частей. Делит слева.

'''
.split() / .rsplit() формирует список
'''

v2 = 'Hello, world, today, is, the, great, day'
print(v2.split())
print(v2.split('o'))
print(v2.split(' ', 1)) #количество символов sep слева, на которые поделить
print(v2.split('l', 2))

#20. .rsplit(sep = None, maxsplit = -1). По умолчанию делит по пробелу. Разделяет строку по sep на maxsplit + 1 частей. Делит справа.

print(v2.rsplit('t', 2))

#21. .join(iterable). Преобразует итерируемый объект, состоящий из строк, в одну строку.

sp = ['Hello', 'world', 'today']

print(','.join(sp)) #необязательно соединять по какому-то символу (можно по подстроке). в итурируемом объекте не должно быть что-то кроме строк.

#Удаление символов

v3 = '                 Hello                '
v4 = '%$#%$#Hello%$#%$#'

#22. .lstrip(chars = None). Удаляет символы в начале. По умолчанию удаляет пробелы
print(v3.lstrip())
print(v4.lstrip('%$#'))

#23 .rstrip(chars = None). Удаляет символы в конце. По умолчанию удаляет пробелы
print(v3.rstrip())
print(v4.rstrip('%$#'))

#24. .strip(chars = None). Удаляет символы в конце и в начале. По умолчанию удаляет пробелы
print(v3.strip())
print(v4.strip('%$#'))

#Проверки (is...) (True / False)

#25. .isalnum(). Проверяет, находятся ли в строке только буквы или цифры.

print(v.isalnum()) #выводит False, так как есть , и пробел

#26. .isalpha(). Проверяет, находятся ли в строке только буквы.

print(v.isalpha())

#27. .isdigit(). Проверяет, находятся ли в строке только цифры.

print(v.isdigit())

#28. .islower(). Проверяет, находится ли вся строка в lowercase.

print(v.islower())

#29. .isupper(). Проверяет, находится ли вся строка в uppercase.

print(v.isupper())

#30. istitle(). Проверяет, находится ли вся строка в titlecase.

print(v.istitle())

'''
f-строки - строки, которые позволяют взаимодействовать со значением переменной.
'''

age = int(input())

s = 'Ваш возраст ' + str(age) + ' лет'
s1 = f'Ваш возраст: {age} года'

print(s)
print(s1)

'''
import ipaddress
p = ipaddress.ip_address('192.192.100.0')
print(f'{p:b}')
'''

#Сравнение строк
print('s' > '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
#сравнение строк лексикографически (сравниваются Unicode-кода). s - 115, 0 - 48. От длины не зависит

print('12345' > '12346')
a = 'A,B323129,321312C'
print(a.split(','))
print(','.join(a.split(',')))
b = 'p6yt312313hon'
print(b.startswith('py'))
print(b.endswith('on'))
n = 'a32b3123c123'
print(n.isalpha())
print(n.isdigit())
print(a.replace(a[1:3], ''), b.replace(b[1:3], ''), n.replace(n[1:3], ''))

a1 = ''
for i in a:
    if not i.isdigit():
        a1 += i
print(a1)

a1 = ''
for i in a:
    if i not in '0123456789':
        a1 += i
print(a1)

import string

a1 = ''
for i in a:
    if i not in string.digits:
        a1 += i
print(a1)

print(string.digits, string.ascii_letters)