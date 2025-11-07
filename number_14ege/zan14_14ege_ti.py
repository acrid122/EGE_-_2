""" 
for x in range(3000, 1, -1):
    v = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    count = 0
    while v > 0:
        if v % 11 == 0:
            count += 1
        v //= 11
    if count == 60:
        print(x)
        break




for x in range(2400, 1, -1):
    v = 7 * 9 ** 210 + 6 * 9 ** 110 - x
    count = 0
    while v > 0:
        if v % 9 == 0:
            count += 1
        v //= 9
    if count == 100:
        print(x)
        break """

""" max_start = max(int('1300220', 4), int('10050', 8), int('1C28', 16))
min_finish = min(int('1333223', 4), int('17750', 8), int('FC28', 16))
for x in range(max_start, min_finish + 1):
    if x // 4 % 4 == 2 and x // 4 ** 2 % 4 == 2 and x // 4 ** 5 % 4 == 3 \
        and x // 4 ** 6 % 4 == 1 and x // 8 ** 4 % 8 == 1 and x % 8 == 0 \
        and x // 8 % 8 == 5 and x % 16 == 8 and x // 16  % 16 == 2 \
        and x // 16 ** 2 % 16 == 12:
        print(x) """


""" s = set()
for x in range(10, 67):
    for y in range(x):
        ch1 = 7 * 67 ** 4 + 3 * 67 ** 3 + x * 67 ** 2 + 1 * 67 + y
        ch2 = 4 * x ** 3 + 9 * x ** 2 + y * x + 6
        v = ch1 + ch2
        s.add(v) #.add() для добавления в множество. множество - неупорядоченная коллекция уникальных элементов
print(len(s)) """
""" import string
s = string.digits + string.ascii_lowercase
for p in range(10, 37):
    for x in s[1:p]:
        for y in s[1:p]:
            ch1 = int(f'{x}{x}{x}8', p)
            ch2 = int(f'43{x}9', p)
            ch3 = int(f'{y}{y}04', p)
            if ch1 + ch2 == ch3:
                print(int(f'{y}{y}{x}', p)) """
                
import string

for x in range(1, 1000):
    v = 27 ** 7 - 3 ** 11 + 36 - x
    s = ''
    s1 = string.digits
    while v > 0:
        s += s1[v % 3]
        v //= 3 
    s = s[::-1]
    #TypeError: int() can't convert non-string with explicit base
    if sum(map(int, s)) == 22:
        print(x)
        break
