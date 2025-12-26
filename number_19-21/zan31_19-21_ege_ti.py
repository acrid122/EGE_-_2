from functools import cache
@cache
def f1(x, y, m):
    if x * y >= 541:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f1(x + 10, y, m - 1), f1(x * 2, y, m - 1), 
          f1(x, y + 10, m - 1), f1(x, y * 2, m - 1)]
    return any(sp) if m % 2 != 0 else all(sp)

print(19, [i for i in range(1, 91) if f1(i, 6, 2)])
print(20, [i for i in range(1, 91) if f1(i, 6, 3) if not f1(i, 6, 1)])
print(21, [i for i in range(1, 91) if f1(i, 6, 4) if not f1(i, 6, 2)])