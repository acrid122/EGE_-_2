with open('26_22605 (1).txt') as f:
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)

sp.sort()

new_sp = []

for i in range(len(sp) - 1):
    x, y = sp[i], sp[i + 1]
    if x[0] == y[0] and x[1] == y[1]:
        new_sp.append((y[2] - x[2], x[0] + x[1]))

new_sp.sort()
'''
[(53, 4552), (160, 11837), (207, 8363), 
(404, 12159), (502, 7721), (560, 7646), 
(607, 12504), (671, 10730), (741, 12625), 
(904, 5345)]
'''
print(new_sp[:10])


with open('26_23570 (2).txt') as f:
    N, K = map(int, f.readline().split())
    homes = list(int(f.readline()) for _ in range(N))
    snow = list(tuple(map(int, line.split())) for line in f)

print(homes[:10])
print(snow[:10])

homes.sort()
snow.sort(key = lambda x: (x[1], -x[0]))

new_snow = [float('inf')] * 1001

for elem in snow:
    new_snow[elem[0]] = min(elem[1], new_snow[elem[0]])

print(new_snow[:10])
summa = 0
max_m = 0

for home in homes:
    mins = min(new_snow[home:])
    summa += mins
    max_m = len(new_snow) - new_snow[::-1].index(mins) - 1

print(summa, max_m)


with open('26_24624 (4).txt') as f:
    N, K = map(int, f.readline().split())
    cinema = list(tuple(map(int, f.readline().split())) for _ in range(N))
    places = list(tuple(map(int, line.split())) for line in f)


cinema.sort()
places.sort()

print(cinema[:10])
print(places[:10])

min_r, count = float('inf'), 0

new_places = []
for i in range(len(places) - 1):
    for j in range(i + 1, len(places)):
        now, nxt = places[i], places[j]
        if nxt[1] - now[1] == 1 and nxt[0] == now[0]:
            break
    else:
        new_places.append(now)
        

print(new_places[:30])
for i in range(1, len(new_places)):
    prev, now = new_places[i - 1], new_places[i]
    if prev[0] == now[0]:
        if prev[1] == now[1]:
            if now[2] - prev[2] >= 6:
                min_r = min(min_r, now[1])
                count += now[2] - prev[2] - 5
        else: #если ряды не равны
            if now[2] >= 6:
                min_r = min(min_r, now[1])
                count += now[2] - 5
            if cinema[prev[0] - 1][2] - prev[2] >= 5:
                min_r = min(min_r, prev[1])
                count += cinema[prev[0] - 1][2] - prev[2]
    else:
        if now[2] >= 6:
                min_r = min(min_r, now[1])
                count += now[2] - 5
        if cinema[prev[0] - 1][2] - prev[2] >= 5:
            min_r = min(min_r, prev[1])
            count += cinema[prev[0] - 1][2] - prev[2]
    
print(min_r, count)


'''
[
(1, 50, 70), (2, 40, 80), (3, 35, 90), (4, 70, 70), 
(5, 70, 80), (6, 45, 50), 
(7, 90, 100), (8, 85, 80), (9, 30, 25), (10, 60, 45)]
'''


