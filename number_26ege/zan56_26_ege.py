'''
9
41 3
50 33
41 125
42 125
43 125
42 126
43 126
50 126
42 127
43 127

41 125
42 125
43 125
'''

with open('26_23383 (1).txt') as f:
    N = int(f.readline())
    sp = set(tuple(map(int, line.split())) for line in f)

sp = sorted(sp, key = lambda x: (x[1], x[0]))

new_sp = [0] * 10 ** 6 #в этом списке индексы будут отвечать за номера контрольных точек

count = 1
for i in range(len(sp) - 1):
    num_p1, num_p2 = sp[i], sp[i + 1]
    if num_p1[1] == num_p2[1] and num_p2[0] - num_p1[0] == 1:
        count += 1
    else:
        if new_sp[num_p1[1]] <= count:
                new_sp[num_p1[1]] = count
        count = 1

print(max(new_sp), new_sp.index(max(new_sp)))

'''
6
10 50
60 90
100 150
110 155
120 160
130 160
90 160
130 170
151 170
'''

'''
10 50 +
60 90
90 160
100 150
110 155
120 160
130 160
130 170
151 170
'''

with open('26_22127.txt') as f:
     N = int(f.readline())
     sp = list(tuple(map(int, line.split())) for line in f)

sp.sort()

count, summa = 0, 0
day = 24 * 60 * 60 * 1000


if sp[0][0] > 0:
     count += 1
     summa += sp[0][0]

cur = sp[0][1]
for start, end in sp:
    if start > cur + 1:
        count += 1
        summa += start - cur - 1
        cur = end
    else:
        cur = max(cur, end)

if cur < day - 1:
     count += 1
     summa += day - cur - 1

print(count, summa)

with open('26_21598.txt') as f:
     N = int(f.readline())
     sp = list(tuple(map(int, line.split())) for line in f)

sp.sort()

new_sp = [0] * 1441
k = []
count, max_count = 0, 0

for start, end in sp:
     new_sp[start] += 1
     new_sp[end] += -1

for i in range(len(new_sp)):
    if new_sp[i] == 0:
        count += 1
    else:
        k.append(i)
        max_count = max(max_count, count + 1)
        count = 0

print(k[-2], max_count)