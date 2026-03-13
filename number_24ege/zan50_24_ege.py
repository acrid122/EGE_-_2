s = open('24.5_19717.txt').readline().strip()

l, count_M, maxs = 0, 0, float('-inf')

for r in range(len(s)):
    if s[r] == 'M':
        count_M += 1
    if count_M > 278:
        maxs = max(maxs, r - l)
        while count_M > 278:
            if s[l] == 'M':
                count_M -= 1
            l += 1

print(maxs)

s = open('24.5_19717.txt').readline().strip()

s = s.split('M')
maxs = float('-inf')
for i in range(len(s) - 278):
    maxs = max(maxs, len('M'.join(s[i : i + 279])))
    #maxs = max(maxs, 278 + sum(len(j) for j in s[i : i + 279]))

print(maxs)

s = open('24_26078.txt').readline().strip()

l, count_2025, count_W, mins = 0, 0, 0, float('inf')

for r in range(len(s)):
    if s[r - 4: r] == '2025':
        count_2025 += 1
    if s[r] == 'W':
        count_W += 1
    if count_2025 == 110:
        if count_W == 90:
            mins = min(mins, r - l)
        while count_2025 == 110:
            if s[l : l + 4] == '2025':
                count_2025 -= 1
                l += 3
            if s[l] == 'W':
                count_W -= 1
            l += 1

print(mins)

s = open('24_26078.txt').readline().strip()

s = s.split('2025')
mins = float('inf')
for i in range(len(s) - 109):
    k = '2025'.join(s[i : i + 110])
    if k.count('W') == 90:
        mins = min(mins, len(k) + 4)

print(mins)

s = open('24_18186.txt').readline().strip()

table = str.maketrans('CDFGHE', 'BBBBBA')
s = s.translate(table).split('BBA')

print(len(max(s, key = len)) + 6)

import re

s = open('24_20813 (1).txt').readline().strip()

s = re.findall(r'(?:[789][7890]*|0)(?:[-*](?:[789][7890]*|0))*', s)

print(len(max(s, key = len)))

s = list(map(str.strip, open('24_7012 (1).txt').readlines())) #.readlines() создает список из строк по \n

count = 0
for line in s:
    q = 'QWERTY'
    pos = 0
    for c in line:
        if c == q[pos]:
            pos += 1
            if pos == 6:
                count += 1
                break
print(count)

s = '7-89*8-0*987'
print(eval(s))