from functools import cache
""" def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x  + 1,y) + f(x + 3, y) + f(x * 2,  y)
print(f(3, 9) * f(9, 12) * f(12, 20)) """

""" def f(x, y, count = 0):
    if x in {24, 32}:
        count += 1
    if x > y:
        return 0
    if x == y and count == 1:
        return 1
    return f(x + 1, y, count) + f(x + 2, y, count) + f(x + 4, y, count) + f(x + 8, y, count)
print(f(16, 48)) """

""" @cache
def f(x, y):
    if x > y:
        return 0
    if  x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 2 + 1, y) + f(x * 10, y)
print(f(1, 15))


 """

@cache
def f()