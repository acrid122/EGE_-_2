from statistics import mean, mode

"""
summa = 0
for i in range(1, 42001):
    s = list(map(int, input().split()))
    '''
    input() - функция ввода с клавиатуры (возвращает введенную строку)
    split() - метод строки, который в данном случае делит строку по пробельному символу. Получается список
    из чисел, которые находятся в строковом формате
    map() - встроенная функция, которая применяет функцию к каждому элементу итерируемого объекта. В данном
    случае к каждому числу в формате строки применяется int(), чтобы строку конвертнуть в число
    list() - встроенная функция, которая конвертит в данном случае map-object в тип list
    '''
    povt = [i for i in s if s.count(i) == 3]
    nepovt = [i for i in s if s.count(i) == 1]
    if len(povt) == 3 and len(nepovt) == 4:
        sr_nepovt = mean(nepovt) #для среднего арифметического
        if sr_nepovt <= povt[0]:
            summa = sum(s)
print(summa)
"""

with open("9_1.txt") as f:
    summa = 0
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) == 3]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) == 3 and len(nepovt) == 4:
            sr_nepovt = mean(nepovt)
            if sr_nepovt <= povt[0]:
                summa = sum(s)
print(summa)


with open('9_2.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) == 3]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) == len(nepovt) == 3:
            if max(s) ** 2 + min(s) ** 2 >= (sum(s) - max(s) - min(s)) ** 2:
                count += 1
    print(count)

with open('9_3.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        povt3 = [i for i in s if s.count(i) == 3]
        povt2 = [i for i in s if s.count(i) == 2]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt3) == 3 and len(povt2) == 2 and len(nepovt) == 2:
            if max(povt3 + povt2) > max(nepovt):
                count += 1
    print(count)
    
with open('9_4.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        tr = [i for i in s if 99 < abs(i) < 1000] #беру модуль, чтобы проверять еще и отрицательные числа (если такие будут)
        if len(tr) >= len(s) / 2:
            if all(i % 5 != 0 for i in s):
                count += 1
    print(count)


with open('9_5.txt') as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) == 2]
        nepovt = [i for i in s if s.count(i) == 1]
        chet = [i for i in s if i % 2 == 0]
        nechet = [i for i in s if i % 2 != 0]
        sr_chet = mean(chet) if len(chet) > 0 else 0
        sr_nechet = mean(nechet) if len(nechet) > 0 else 0
        fl1 = len(povt) == 2 and len(nepovt) == 4
        fl2 = abs(sr_chet - sr_nechet) > 50
        if fl1 != fl2:
            count += 1
    print(count)

from collections import Counter

a = [1, 2, 2, 2, 1, 3]
print(Counter(a))
print(mode(a))

from statistics import mean
with open("9_6.txt") as f:
    res = 0
    for number, i in enumerate(f, 1):
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) != 1]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) > 0 and len(nepovt) > 0 and sum(s) % 2 != 0 and sum(povt) ** 2 > sum(nepovt) ** 2:
            res = number
print(res)