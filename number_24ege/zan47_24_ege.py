import string

p = string.digits

s = 'X004000XXX12XXXXX2000XXXXX3001XXX'

l, r = 0, 0
sp = []
maxs = float('-inf')

while l < len(s):
    if s[l] != '0' and s[l] in p:
        r = l
        while r < len(s) and s[r] in p:
            r += 1
        sp.append(s[l : r])
        maxs = max(maxs, int(s[l : r]))
        l = r
    else:
        l += 1

print(sp, maxs)

import string

p = string.printable[:14]

with open('24_26551.txt') as f:
    s = f.readline().strip() #.readline() - считывание одной строки

#s = 'XXX08329XXXX743823XXX1239012XXX123'
'''
832
74382
1239012
12
'''

l, r = 0, 0
maxs = float('-inf')
sp = []

while l < len(s):
    if s[l] in p and s[l] != '0': #число не может начинаться с нуля
        r = l
        while r < len(s) and s[r] in p:
            if int(s[r], 14) % 2 == 0:
                #p_index = r
                maxs = max(maxs, r - l + 1)# 12: r = 1, l = 0
                #sp.append(s[l : r + 1]) #7 ['8', '832', '74', '7438', '74382', '12', '12390', '1239012', '12']
            r += 1
        #maxs = max(maxs, p_index - l + 1)
        l = r
    else:
        l += 1

print(maxs, sp)


with open('24_26549.txt') as f:
    s = f.readline().strip()

#s = 'XY2025YXX2025YYXXYXY2025XXX2025XXXX2025Y2025XY2025' #2025 ровно 2 раза, Y не менее 2. чтобы оканчивалось на 2025.

'''
XY2025YXX2025 | XY2025YXX2025YYXXYXY202 - если бы не было условия про то, что оканчивается на 2025
025YXX2025YYXXYXY2025
025YYXXYXY2025XXX2025
025XXX2025XXXX2025
025XXXX2025Y2025
025Y2025XY2025
'''

l, count_2025, count_y = 0, 0, 0
maxs = float('-inf')

for r in range(len(s)):
    if s[r - 4: r] == '2025':
        count_2025 += 1
    if s[r] == 'Y':
        count_y += 1
    
    if count_2025 == 50:
        if count_y >= 140:
            maxs = max(maxs, r - l)
        while count_2025 == 50:
            if s[l : l + 4] == '2025':
                count_2025 -= 1
            if s[l] == 'Y':
                count_y -= 1
            l += 1
print(maxs) 


with open('24_26077.txt') as f:
    s = f.readline().strip()

#s = 'XXXG727G34XXX7234G99G8735G44G890219GGXXG789000XXG888G' #Ровно 2 нечетных
'''
G727
G34XXX72
G99
G873
G89021
G789000XX
'''

import string

p = string.digits

l = 0
maxs = float('-inf')
sp = []

while l < len(s):
    if s[l] == 'G':
        r = l + 1
        count_odd, count_g = 0, 0
        while r < len(s):
            if s[r] in p and int(s[r]) % 2 != 0:
                count_odd += 1
                if count_odd == 46:
                    count_odd -= 1
                    break
            if s[r] == 'G':
                break
            r += 1
        if count_odd == 45:
            sp.append(s[l : r])
                #print(sp)
            maxs = max(maxs, r - l)
        l = r
    else:
        l += 1

print(maxs)
print(max(sp, key = len))
