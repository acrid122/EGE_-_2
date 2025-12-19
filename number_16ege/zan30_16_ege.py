"""
Фибоначчи без мемоизации

def fib(n):
    if n == 1: return 0
    if n == 2: return 1
    return fib(n - 2) + fib(n - 1)
print(fib(39))
"""

#Чтобы добавить мемоизацию, надо использовать декоратор. Декоратор - просто надстройка над функцией.
from functools import cache #cache - декоратор, который добавляет возможность функции кэшировать значения

@cache #декоратор указывает сверху над определением функции через @
def fib(n):
    if n == 1: return 0
    if n == 2: return 1
    return fib(n - 2) + fib(n - 1)
print(fib(150))

#Любую рекурсию можно переписать итеративно. И любой итеративный алгоритм можно переписать в рекурсию

sp = [0] * 151
sp[1], sp[2] = 0, 1
for i in range(3, 151):
    sp[i] = sp[i - 2] + sp[i - 1]
print(sp[150])


#мемоизация никакой роли не сыграет, так как все вызовы уникальные
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#16_24891
from sys import setrecursionlimit

setrecursionlimit(9000)

#@cache #для мемоизации. кэширование результатов второй функции (чтобы брались результаты из кэша). НАДО ПОСМОТРЕТЬ, ПОЧЕМУ ЛОМАЕТСЯ
def f1(n):
    if n <= 10: return n
    return n - 7 + f1(n - 21)

#RecursionError: maximum recursion depth exceeded. Превышена глубина рекурсии
'''
(185734 - 10) / 21 + 1 = 8855
'''
print((f1(185734) - f1(185650)) / f1(40))

'''
def f1(n):
    if n <= 0: return n
    return n - 7 + f1(n - 1)

f1(4) -> f1(3) -> f1(2) -> f1(1) -> f1(0)

4 / 1 + 1 = 5

def f1(n):
    if n <= 2: return n
    return n - 7 + f1(n - 1)

f1(4) -> f1(3) -> f1(2)

(4 - 2) / 1 + 1 = 3
'''

sp1 = [0] * 185735 #чтобы был индекс 185734

for i in range(185735):
    if i <= 10:
        sp1[i] = i
    else:
        if i - 21 < 0:
            sp1[i] = i - 7 + (i - 21)
        else:
            sp1[i] = i - 7 + sp1[i - 21]

print((sp1[185734] - sp1[185650]) / sp1[40])

setrecursionlimit(100000)

def f2(n):
    if n < 19: return 6 * (g2(n - 7) - 36)
    return f2(n - 4) + 3580

def g2(n):
    if n >= 248045: return n / 20 + 28
    return g2(n + 9) - 4

#RecursionError: maximum recursion depth exceeded
print(f2(673))

fp2 = [0] * 674
gp2 = [0] * 250001

for i in range(250_000, -1, -1):
    if i >= 248045:
        gp2[i] = i / 20 + 28
    else:
        gp2[i] = gp2[i + 9] - 4

for i in range(674):
    if i < 19:
        fp2[i] = 6 * (gp2[i - 7] - 36)
    else:
        fp2[i] = fp2[i - 4] + 3580

print(fp2[673])