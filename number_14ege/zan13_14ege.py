'''
Минимальная СС, которая поддерживается в Питоне - 2 СС, максимальная 36 СС.
'''
ch1 = '22A12E'
ch2 = '2F1391'
ch3 = '1H05D0'
print(max(max([ch1, ch2, ch3], key = max)))

import string

s = string.digits + string.ascii_uppercase
#012345...
number_H = s.index('H') + 1 #минимальная СС, где может быть H
for p in range(number_H, 37):
    ch1 = int('22A12E', p)
    ch2 = int('2F1391', p)
    ch3 = int('1H05D0', p)
    v = ch1 + ch2 - ch3
    if v % 19 == 0:
        print(v // 19)
        break #так как надо наименьшее p


s = string.digits + string.ascii_uppercase
#s = '012345...
#for x in s[:3]
for x in s[:29][::-1]: #до 29 индекса, так как в 29 СС (для наибольшего либо переворачиваем s[:29][::-1], либо без break и смотрим последний ответ)
    ch1 = int(f'923{x}874', 29)
    ch2 = int(f'524{x}6152', 29)
    v = ch1 + ch2
    if v % 28 == 0:
        print(v // 28)
        break


for x in range(67, -1, -1): #перевернули, чтобы применить break и найти max x
    ch1 = 68 ** 0 * 5 + 68 ** 1 * x + 68 ** 2 * 3 + 68 ** 3 * 2 + 68 ** 4 * 1
    ch2 = 68 ** 0 * 3 + 68 ** 1 * 3 + 68 ** 2 * 2 + 68 ** 3 * x + 68 ** 4 * 1
    v = ch1 + ch2
    if v % 12 == 0:
        print(v // 12)
        break


s = string.digits + string.ascii_uppercase
for x in s[1:11]: #наименьшая СС, идем с 1 индекса, так как число не может начинаться с нуля
    ch1 = int(f'3364{x}', 11)
    ch2 = int(f'{x}7946', 12)
    ch3 = int(f'55{x}87', 14)
    if ch1 + ch2 == ch3:
        print(ch3)
        break


s = string.digits + string.ascii_uppercase
sp = []
for x in s[:21]:
    for y in s[:21]:
        ch1 = int(f'943697{x}21', 21)
        ch2 = int(f'2{y}9253', 21)
        v = ch1 - ch2
        if v % 20 == 0:
            sp.append((x, y, int(x, 21) - int(y, 21)))
#elem = max(sp, key = lambda x: x[2])
sp.sort(key = lambda x: -x[2])
ch1 = int(f'943697{sp[0][0]}21', 21)
ch2 = int(f'2{sp[0][1]}9253', 21)
print((ch1 - ch2) // 20)


for x in range(6):
    for y in range(1, 6):
        ch1 = int(f'10{x}{y}{x}', 6)
        ch2 = int(f'{y}11{x}', 7)
        if ch1 == ch2:
            print(x + y)


s = 2 * 2187 ** 2020 + 729 ** 2021 - 2  * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
count = 0
while s > 0:
    if s % 27 > 9:
        count += 1
    s //= 27
print(count)

s = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
count = 0
while s > 25:
    if s % 25 == 0:
        count += 1
    s //= 25
print(count)