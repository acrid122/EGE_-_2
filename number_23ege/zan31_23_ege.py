def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y)

print(f(1, 5))

def f1(x, y):
    #x - какое-то текущее значение в последовательности, y - конечное значение
    if x > y or x == 43:
        return 0 #это показатель того, что последовательность не подошла
    if x == y: 
        return 1 #это показатель того, что последовательность подошла
    return f1(x + 2, y) + f1(x + x - 1, y) + f1(x + x + 1, y)

print(f1(7, 63))

def f2(x, y, s = ''):
    if x > y + 2 or s[-3:] == 'AAA':
        return 0
    if x == y:
        return 1
    return f2(x - 1, y, s + 'A') + f2(x + 5, y, s + 'B') + f2(x * 2, y, s + 'C')

print(f2(5, 34))    

def f2(x, y, s = ''):
    if x > y + 2 or s == 'AAA':
        return 0
    if x == y:
        return 1
    return f2(x - 1, y, s[-2:] + 'A') + f2(x + 5, y, s[-2:] + 'B') + f2(x * 2, y, s[-2:] + 'C')

print(f2(5, 34))    

def f3(x, y):
    if x > y or x == 21:
        return 0                    
    if x == y: return 1
    return f3(x + 1, y) + f3(x * 3, y) + f3(x * 4, y)

print(f3(2, 16) * f3(16, 60))

def f3(x, y, sp = []):
    if x > y or 21 in sp:
        return 0
    if x == y and 16 in sp: 
        return 1
    return f3(x + 1, y, sp + [x + 1]) + f3(x * 3, y, sp + [x * 3]) + f3(x * 4, y, sp + [x * 4])
print(f3(2, 60))

def f4(x, y, s = ''):
    if x < y or 'AAA' in s or 'BBB' in s:
        return 0
    if x == y:
        return 1
    if x % 2 == 0:
        return f4(x - 2, y, s[-2:] + 'A') + f4(x / 2, y, s[-2:] + 'B')
    else:
        return f4(x - 2, y, s[-2:] + 'A') + f4(x - 7, y, s[-2:] + 'B')

print(f4(40, 1))

def f5(x, y, count = 0):
    if x in {40, 30, 20}:
        count += 1
    if x < y:
        return 0
    if x == y and count >= 2:
        return 1
    return f5(x - 1, y, count) + f5(x - 3, y, count) + f5(x // 3, y, count - 1)

print(f5(49, 12))

def f6(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    d = x // 10 % 10
    e = x % 10
    if d < e:
        return f6(x + 1, y) + f6(x // 100 * 100 + e * 10 + d, y)
    return f6(x + 1, y)

print(f6(101, 154))