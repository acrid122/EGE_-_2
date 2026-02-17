from itertools import *

def f(x, y, w, z):
    return (x or y) and not(y == z) and not w

sp = permutations("xywz")

for x1, x2, x3, x4 in product([0, 1], repeat = 4):
    table = [
        (1, x1, 1, x2),
        (0, 1, x3, 0), 
        (x4, 1, 1, 0)
    ]
    if len(table) == len(set(table)):
        for p in sp:
            if all(f(**dict(zip(p, line))) for line in table):
                print(*p)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
c = [9, 10, 11, 12, 13, 14]
print(list(zip(a, b, c)))


def f1(x, y, w, z):
    print(x, y, w, z)

s = (1, 1, 1, 0)
p = 'xywz'
print(f1(**dict(zip(p, s))))
#{'x': 1, 'y': 1, 'w': 1, 'z': 0}
print(f1(x = 1, y = 1, w = 1, z = 0))

from itertools import *

def f2(x, y, w, z):
    return not((z <= y) or ((w <= x) <= y))

for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6):
    table = [
        (x1, 0, 0, x2), 
        (x3, x4, 1, x5), 
        (x6, 1, 1, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if all(f2(**dict(zip(p, line))) for line in table):
                print(*p)


from itertools import *

def f3(x, y, w, z):
    return (((not y) <= (not w)) <= (not z)) <= x

for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
    table = [
        (x1, 1, x2, 1, 0),
        (0, 1, x3, 0, 1),
        (x4, x5, 1, 0, 0)
    ] 
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if all(f3(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)

print("x y w z")

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not((((not y) <= (not w)) <= (not z)) <= x):
                    print(x, y, w, z)