#Общий подсчет делителей числа

#36 = 1, 2, 3, 4, 6, 9, 12, 18, 36 - 9 штук

def bad_count_divisors(x): #принимает одно число (то число, количество делителей которого надо посчитать)
    count = 0
    for d in range(1, x + 1):
        if x % d == 0:
            count += 1
    return count


print(bad_count_divisors(36))

'''
36

1 | 36
2 | 18
3 | 12
4 | 9
6

Главная оптимизация заключается в том, чтобы рассматривать диапазон делителей до корня числа. Если мы идем до корня, то можно найти
абсолютно все делители
'''

def good_count_divisors(x):
    count = 0
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            if d != x // d:
                count += 2
            else:
                count += 1
    return count


print(good_count_divisors(36))


#Если важно знать все делители или какую-то часть
import math


def good_find_divisors(x):
    s = set() #лучше использовать множество, так как это коллекция уникальных объектов
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            s.add(d)
            s.add(x // d)
    return s, len(s), sum(s), math.prod(s)


print(good_find_divisors(36))


#Алгоритм проверки числа на простоту

def is_prime(x):
    if (x % 2 == 0 and x != 2) or x < 2: #любое четное число за исключением 2 или меньше 2
        return False
    for d in range(3, int(x ** .5) + 1, 2): #проверяем только нечетные делители
        if x % d == 0:
            return False
    return True


print(is_prime(36), is_prime(2), is_prime(-9), is_prime(109))


#Взаимно простые - те числа, у которых НОД = 1


def good_find_divisors(x):
    s = set() #лучше использовать множество, так как это коллекция уникальных объектов
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            s.add(d)
            s.add(x // d)
    return s


def relatively_prime(s1, s2):
    return (s1 & s2) == {1} #& - пересечение множеств


s1 = good_find_divisors(36)
s2 = good_find_divisors(19)
print(relatively_prime(s1, s2))


#Факторизация - алгоритм разложения числа на простые множители

#36 = 2 ** 2 * 3 ** 2

'''
Обычный словарь0

p = {
    'А': 20,
    'Б': 21,
    'В': 19
}

print(p['А'])

print(p['Г']) - будет ошибка, так как ключа не существует

p['Г'] += 1 - все равно будет ошибка
'''

from collections import defaultdict


#defaultdict решает эту проблему, так как у несуществующих ключей есть значения по умолчанию
#int - тип значения по умолчанию, если int, то 0

def fact(x):
    '''
    36 = {
        2: 2, 
        3: 2
    }
    '''
    factors = defaultdict(int)
    d = 2
    while x % d == 0:
        factors[d] += 1
        x //= d
    
    for d in range(3, int(x ** .5) + 1, 2):
        while x % d == 0:
            factors[d] += 1
            x //= d

    if x > 1:
        factors[x] = 1

    return factors
print(fact(16), fact(36), fact(7))
#defaultdict(<class 'int'>, {1: 1})


#Подсчет количества делителей числа

'''
Математическая формула:

N = 2 ** p * e1 ** p1 * e2 ** p2 * ... * en ** pn

Количество = (p + 1) * (p1 + 1) * (p2 + 1) * ... * (pn + 1)
Количество_нечетных = (p1 + 1) * (p2 + 1) * ... * (pn + 1)
Количество_четных = Количество - количество_нечетных = p * (p1 + 1) * (p2 + 1) * ... * (pn + 1)

36 = 2 ** 2 * 3 ** 2

Количество_36 = (2 + 1) * (2 + 1) = 3 * 3 = 9
Количество_нечетных_36 = 2 + 1 = 3 | 1, 3, 9
Количество_четных_36 = 9 - 3 = 6
'''

def count_divisors_from_fact(x):
    factors = fact(x)
    #defaultdict(<class 'int'>, {2: 2, 3: 2})
    total_divisors = 1
    for exp in factors.values(): #factors.values() - возвращает список значений словаря
        total_divisors *= (exp + 1)


    odd_divisors = total_divisors // (factors[2] + 1)
    even_divisors = total_divisors - odd_divisors

    return total_divisors, odd_divisors, even_divisors


print(count_divisors_from_fact(36))


'''
Сколько существует чисел в диапазоне от 10**9, 2 * 10**9, которые можно представить в виде N = 2 ** m * 3 ** n, где m - число четное, n - число нечетное.
'''
start = 10 ** 9
finish = 2 * 10 ** 9

count = 0
for m in range(2, 41, 2):
    for n in range(1, 41, 2):
        if start <= 2 ** m * 3 ** n <= finish:
            count += 1
print(count)


'''
Найти все числа, у которых ровно три нетривиальных делителя. Нетриваиальными делителями обычно считаются числа, которые отличны от единицы и делимого.

Количество = (p + 1) * (p1 + 1) * (p2 + 1) * ... * (pn + 1) = 5 -> понимаем, что только 1 множитель, а связанная степень будет равняться 4

N = e ** 4.
'''

for number in range(10 ** 9, 2 * 10 ** 9):
    if number ** (1 / 4) == int(number ** (1 / 4)):
        break

'''
Количество = 3
N = e ** 2 -> (2 + 1) = 3

Количество = 8

N = e1 * e2 * e3 -> (1 + 1) * (1 + 1) * (1 + 1) = 8
N = e1 ** 3 * e2 -> (3 + 1) * (1 + 1) = 8
...
'''

#НОД и НОК

from math import lcm, gcd

#gcd - НОД
#lcm - НОК

print(gcd(36, 12))
print(lcm(36, 12))

