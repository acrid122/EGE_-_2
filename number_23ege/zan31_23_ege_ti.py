from functools import cache
@cache
def f(x, y, count = 0):
    if x in {24, 32}:
        count += 1
    if x > y: 
        return 0
    if x == y and count == 1:
        return 1
    return f(x + 1, y, count) + f(x + 2, y, count) + f(x + 4, y, count) + f(x + 8, y, count)
print(f(16, 48))



def f2(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f2(x + 1, y) + f2(x + 3, y) + f2(x * 2, y)
print(f2(3, 9) * f2(9, 12) * f2(12, 20)) 



def f3(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f3(x + 1, y) + f3(x * 2, y) + f3(x * 2 + 1, y) + f3(x * 10, y)
    
print(f3(1, 15))



def f4(x, y):
    if x > y:
        return 0
    if x == y: 
        return 1
    if x // 10 % 10 < x % 10:
        x = str(x)
        x = x[:-2] + x[-1] + x[-2]
        x = int(x)
        return f()
print(f4(101, 154))