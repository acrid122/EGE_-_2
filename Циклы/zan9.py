'''
Цикл for используется для перебора элементов итерируемого объекта (списка, кортежа, строки, диапазона и т.д.)

for variable in itreable:
    #Код
'''

lst = [1, 2, 3]
for elem in lst:
    print(elem, end = ' ') #end - параметр print(), который задает символ после вывода

print()

for elem in lst:
    elem = 1 #elem - копия элемента списка. в данном случае просто меняется копия
print(lst)

'''
range(start = 0, stop, step = 1)

stop невключительно

1. range(5) -> 0, 1, 2, 3, 4
2. range(1, 5) -> 1, 2, 3, 4
3. range(1, 5, 2) -> 1, 3
'''

for i in range(len(lst)): #range(len(lst)) = range(3) = 0, 1, 2
    lst[i] = 1
print(lst)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for elem in row:
        elem = 1
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = 1
print(matrix)

#Нюансы

'''
Не надо изменять итерируемый объект внутри цикла (remove, append, pop, replace (если на пустую) и т.д.)

lst = [1, 2, 3]
for elem in lst:
    lst.append(4)
'''

'''
Цикл while. Цикл по условию. Выполняется, пока условие истинно.

while condition:
    ....

Нюансы:
1) Угроза бесконечно цикла.
2) Нет захода в цикл.
'''

#1 нюанс
x = 0
while x < 5:
    print(x)
    x += 1 #инкремент, увеличение на 1

#2 нюанс

x = 0
while x > 5:
    print(x)
    x -= 1

#Бесконечный цикл

'''
while True:,  while 1
'''

#break/continue

#break - оператор досрочного выхода из цикла (прерывание цикла)

for x in range(6):
    if x == 3:
        break
    print(x)

print()

for x in range(6):
    print(x)
    if x == 3:
        break

print()

for x in range(6):
    if x == 3:
        print(x)
        break

print()

for x in range(6):
    if x == 3:
        break
        print(x)

#continue - оператор, который пропускает текущую итерацию и переходит к следующей. При срабатывании пропускает все строчки кода, находящиеся под ним в рамках цикла

for x in range(6):
    if x == 3:
        continue
    print(x)

print()

for x in range(6):
    print(x)
    if x == 3:
        continue

print()

for x in range(6):
    if x == 3:
        print(x)
        continue

print()

for x in range(6):
    if x == 3:
        continue
        print(x)

#break и cotinue в рамках while работают точно также

'''
x = 0
while x <= 5:
    if x == 3:
        x += 1
        continue #надо быть аккуратным, так как continue пропустит и инкремент если не написать 152 строку
    print(x)
    x += 1
'''

#for-else, while-else

#for-else

'''
Если внутри цикла срабатывает break, то блок кода, описанный в else не выполняется, иначе выполняется.
'''

lst = [i for i in range(1, 5)]
for elem in lst:
    if elem == 10:
        print('Найдено')
        break
else:
    print('Не найдено')

i = 0
while i < len(lst):
    if lst[i] == 2:
        print('Найдено')
        break
    i += 1
else:
    print('Не найдено')

names = ['Alice', 'Anna', 'Bob', 'John']
scores = [90, 80, 70, 60]

print(list(zip(names, scores)))

for i in zip(names, scores):
    print(i)

'''
for i in zip(names, scores):
    for j in i:
'''
#a, b = (1, 2)

for name, score in zip(names, scores):
    print(name, score)

matrix = [
    ['Alice', 90, 18],
    ['Bob', 80, 17],
    ['Anna', 70, 19]
]

#a, b, c = [1, 2, 3]

for name, score, age in matrix:
    print(name, score, age)

#enumerate(iterable, start = 0). возвращает итератор кортежей. (индекс, элемент)

lst = [90, 80, 70]
#90 - 0, 80 - 1, 70 - 2

print(list(enumerate(lst)))

for index, elem in enumerate(lst):
    print(index, elem)

for index, elem in enumerate(lst, 1000):
    print(index, elem)

'''
Сумма чётных чисел
Вход: lst = [1, 2, 3, 4]
Задача:

Используйте for для подсчёта суммы чётных чисел.
Выведите: f"Список: {lst}, сумма чётных: {total}".
'''
lst = [1, 2, 3, 4]

total = 0
for x in lst:
    if x % 2 == 0:
        total += x

print(f"Список: {lst}, сумма чётных: {total}")

total = sum([x for x in lst if x % 2 == 0])
print(f"Список: {lst}, сумма чётных: {total}")

'''
Поиск первого отрицательного
Вход: lst = [1, 2, -3, 4]
Задача:

Используйте while для поиска первого отрицательного числа.
Если найдено, прервите цикл с break.
Выведите: f"Список: {lst}, первое отрицательное: {result}".
'''


lst = [1, 2, -3, 4]
x = 0
while lst[x] >= 0:
    x = x + 1
result = lst[x]
print(f"Список: {lst}, первое отрицательное: {result}")

'''
Пропуск нечётных
Вход: lst = [1, 2, 3, 4]
Задача:

Используйте for с continue для вывода только чётных чисел.
'''
lst = [1, 2, 3, 4]

for x in lst:
    if x % 2 != 0:
        continue
    print(x)

'''
Проверка на нули
Вход: lst = [1, 0, 3]
Задача:

Используйте for с else для проверки наличия нулей.
Если нули есть, прервите цикл.
Выведите: f"Список: {lst}, нули есть: {has_zeros}".
'''

lst = [1, 0, 3]
for x in lst:
    if x == 0:
        has_zeros = True
        break
else:
    has_zeros = False
print(f"Список: {lst}, нули есть: {has_zeros}")

'''
Удвоение элементов матрицы
Вход: matrix = [[1, 2], [3, 4]]
Задача:

Используйте вложенный for для удвоения каждого элемента.
Выведите: f"Матрица: {matrix}".
'''
matrix = [[1, 2], [3, 4]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] *= 2

print(matrix)

'''
Объединение списков
Вход: lst1 = [1, 2], lst2 = ["a", "b"]
Задача:

Используйте zip для создания пар (число, строка).
Выведите: f"Пары: {pairs}".
'''

lst1 = [1, 2]
lst2 = ["a", "b"]
pairs = list(zip(lst1, lst2))
print(f"Пары: {pairs}")

'''
Транспонирование матрицы
Вход: matrix = [[1, 2], [3, 4]]
Задача:

Используйте zip(*matrix) для транспонирования.
Выведите: f"Транспонированная: {transposed}".
'''

'''
1 2
3 4 ->
1 3
2 4
'''
matrix = [[1, 2], [3, 4]]
transposed = list(zip(*matrix)) #* - распаковка zip(*matrix) -> zip([1, 2], [3, 4])
print(f"Транспонированная: {transposed}")

'''
Удвоение по индексу
Вход: lst = [1, 2, 3]
Задача:

Используйте enumerate для удвоения элементов с чётными индексами.
Выведите: f"Список: {lst}"
'''
lst = [1, 2, 3]
lst2 = []
for index, elem in enumerate(lst):
    if index % 2 == 0:
        lst2.append(elem * 2)
    else:
        lst2.append(elem)

print(lst2)

lst = [1, 2, 3]
for index, _ in enumerate(lst):
    if index % 2 == 0:
        lst[index] *= 2
print(lst)

'''
Объединение трёх списков
Вход: lst1 = [1, 2], lst2 = ["a", "b"], lst3 = [True, False]
Задача:

Используйте zip для создания тройных кортежей.
Выведите: f"Тройки: {triples}".
'''
lst1, lst2, lst3 = [1, 2], ["a", "b"], [True, False]

triples = list(zip(lst1, lst2, lst3))

#zip(lst1, lst2) -> [(1, 'a'), (2, 'b')]
#zip([(1, 'a'), (2, 'b')], [True, False]) -> [([(1, 'a'), (2, 'b')], True)]

print(f"Тройки: {triples}")
'''
Сравнение элементов
Вход: lst1 = [1, 2], lst2 = [2, 1]
Задача:

Используйте zip для проверки, где элементы различаются.
Выведите: f"Различия: {differences}".

[1, 2], [2, 1], [3, 2] .... [4, 5]
'''
import random

lst = [(random.randint(0, 6), random.randint(0, 6)) for _ in range(1000)]
#[(2, 6), (5, 1), (1, 2), (4, 2), (0, 3), (2, 4), (2, 3), (2, 2), (4, 2), (5, 2)] первые 10


differences = 0
n = len(lst)
for i in range(n):
    for j in range(i + 1, n):
        a, b = zip(lst[i], lst[j])
        if a[0] != b[0]:
            differences += 1
        if a[1] != b[1]:
            differences += 1
print(f"Различия: {differences}")

a, b, c = (2, 6), (5, 1), (1, 2)
print(a, b, c)

'''
0: 2 5 1
1: 6 1 2
'''

print(list(zip(a, b, c)))