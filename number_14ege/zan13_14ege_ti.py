'''for p in range(7, 37):
    ch1 = int('2465123', p)
    ch2 = int('251341', p)
    v = ch1 + ch2
    if v % 17 == 0:
        print(v // 17)
        break


'''
'''
v = 17 * 125 ** 453 + 117 * 5 ** 231 - 3 * 5 ** 13 - 2357
count = 0
while v > 0:
    if v % 125 <= 37:
        count += 1
    v //= 125
print(count)
'''

''''
v= 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
count = 0
while v > 0:
    if v % 49 <= 9:
        count += 1
    v //= 49
print(count)
'''


""" v= 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
count = 0
while v > 0:
    if v % 49 <= 9:
        count += 1
    v //= 49
print(count) """


""" import string
s = string.digits + string.ascii_lowercase
for x in s[:29]:
    ch1 = int(f'463{x}7921', 29)
    ch2 = int(f'8241{x}153', 29)
    v = ch1 + ch2
    if v % 28 == 0:
        print(v // 28)
        break """



""" import string
s = string.digits + string.ascii_lowercase
for x in s[:14]:
    ch1 = int(f'4B3{x}1', 14)
    ch2 = int(f'5{x}F83', 16)
    v = ch1 + ch2
    if v % 13 == 0:
        print(v // 13)
        break """




""" import string
s = string.digits + string.ascii_lowercase
for x in s[1:13]:
    ch1 = int(f'9{x}AB', 13)
    ch2 = int(f'{x}46C', 16)
    ch3 = int(f'B7{x}', 15)
    v = ch1 + ch2 - ch3
    if v % 14 == 0:
        print(v // 14)
        break """

 
""" import string
s = string.digits + string.ascii_lowercase
for p in range(10, 37):
    for x in s[1:p]:
        for y in s[1:p]:
            ch1 = int(f'24{x}9', p)
            ch2 = int(f'{y}{x}{y}3', p)
            ch3 = int(f'{x}4{y}0', p)
            if ch1 + ch2 == ch3:
                print(int(f'{x}{y}{y}', p)) """



""" for p in range(8, 37):
    ch1 = int('11353712', p)
    ch2 = int('135421', p)
    v = ch1 + ch2
    if v % 31 == 0:
        print(v // 31)
        break """



""" v = 39 * 121 ** 319 + 46 * 11 ** 913 - 15 * 1331 ** 15 - 1993
count = 0
while v > 0:
    if v % 121 >= 64 and v % 121 <= 104:
        #64 <= x % 121 <= 104
        count += 1
    v //= 121
print(count) """


""" 
import string
s = string.digits + string.ascii_lowercase
for x in s[:21]:
    ch1 = int(f'82934{x}2', 21)
    ch2 = int(f'2924{x}{x}7', 21)
    ch3 = int(f'67564{x}8', 21)
    v = ch1 + ch2 + ch3
    if v % 20 == 0:
        print(v // 20)
        break """

















