""" from collections import defaultdict
def f(n):
    d = 2
    fact = defaultdict(int)
    while d ** 2 <= n:
        if n % d == 0:
            fact[d] += 1
            n //= d
        else:
            d += 1
    fact[n] += 1
    return fact
count = 0
for n in range(10 ** 6 + 1, 10 ** 8):
    summ = 0
    if count == 5:
        break
    s = f(n)
    if s[2] >= 20:
        if len(s) > 1:
            for i in s:
                if i == 2:
                    continue
                summ += i ** s[i]
                #{2:21, 3:2}
            print(n, summ)
        else:
            print(n, 0)
        count += 1 """

summa = 0
for i in range(0, 20):
    summa += 3 * 2 ** i
print(summa)

def is_prime(x):
    if (x % 2 == 0 and x != 2) or x < 2:
        return False
    for d in range(3, int(x ** .5) + 1, 2):
        if x % d == 0:
            return False
    return True


def find_del(x):
    s = set()
    for d in range(1, int(x ** .5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                s.add(d)
            if x // d % 2 == 0:
                s.add(x // d)
    return sorted(s)[1]

for i in range(113_000_000, 114_000_000 + 1):
    if (is_prime(i ** (1 / 3)) and i ** (1/3) == int(i ** (1 / 3))) \
        or (is_prime(((i / 2) ** (1 / 2))) and ((i / 2) ** (1 / 2)) == int((i / 2) ** (1 / 2))):
        print(i, find_del(i))

print(113040648 ** (1/3))
print((113040648 / 2) ** (1/2))


with open('17_18257.txt') as f:
    sp = list(map(int, f))
count = 0
ras = float('inf')
max_in_sp = max(sp)


#[1, 2, 3, 4] - (1, 2), (1, 3), (1, 4)
#(2, 3), (3, 4)
for i in range(len(sp) - 1):
    for j in range(i + 1, len(sp)):
        x, y = sp[i], sp[j]
        if (i + j + 2) % 10 == max_in_sp % 10:
            count += 1
            ras = min(abs((x + y) - (i + j + 2)), ras)

print(count, ras)

with open('17_25356 (1).txt') as f:
    sp = list(map(int, f)) #чтобы получить список чисел

count, max_s = 0, float('-inf') #максимум инициализируем минимальным значением, а минимум - максимальным
max_30 = max(i for i in sp if abs(i) % 100 == 30) #все остатки от деления берем от модуля числа, так как остатки от отрицательных чисел в математике берутся иначе

def check_four(x):
    return 1000 <= abs(x) <= 9999

for i in range(len(sp) - 2): #чтобы не было ошибки - отсекаем лишние индексы
    x, y, z = sp[i:i+3] #sp[i], sp[i + 1], sp[i + 2] 
    '''
    5 способ, как посчитать количество 4-значных.

    Вынести в отдельную функцию проверку на 4-значность.

    Вызывать функцию для каждого числа. Функция логическая (возвращает True/False). Сложить результаты.

    Логические значения можно складывать между собой. True + True = 2

    (check_four(x) + check_four(y) + check_four(z)) == 0
    '''
    if (check_four(x) + check_four(y) + check_four(z)) == 0 and (x + y + z) > max_30:
        count += 1
        max_s = max(x + y + z, max_s)
print(count, max_s)

with open('17_9070.txt') as f:
    sp = list(map(int, f))


count, min_s = 0, float('inf')

mit_tr = min(i for i in sp if len(str(i)) == len(set(str(i))) == 3)


#1, 2, 3, 4 -> 1, 4 / 2, 3 


for i in range(len(sp) // 2):
    x, y = sp[i], sp[len(sp) - i - 1]
    if x * y % mit_tr == 0:
        count += 1
        min_s = min(min_s, x + y)

print(count, min_s)

#невозрастание - убывание, но с повторениями 333322221111
#строгое убывание - убывание без повторений 321

with open('17_001.txt') as f:
    sp = list(map(int, f))

count, min_s = 0, float('inf')
sum_min = sum(map(int, str(min(i for i in sp if list(str(i)) == sorted(str(i), reverse = True) \
                               and len(str(i)) == len(set(str(i)))))))

def soft_increase(i):
    return list(str(i)) == sorted(str(i)) and len(str(i)) == len(set(str(i)))
 
for i in range(len(sp) - 1):
    x, y = sp[i : i + 2]
    if soft_increase(x) + soft_increase(y) == 1 and x * y % sum_min == 0:
        count += 1
        min_s = min(min_s, x + y)

print(count, min_s)