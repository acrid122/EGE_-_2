#Начальная координата 1 прямоугольника: 0, 0
#Максимальная координата 1 прямоугольника: 22, 16

#Начальная координата 2 прямоугольника: 5, 5
#Конечная координата 2 прямоугольника: 5 + 77, 5 + 52

def rect(x1, y1, x2, y2):
    return {(x, y) for x in range(min(x1, x2  ), max(x1, x2) + 1) for y in range(min(y1, y2), max(y1, y2) + 1)}

r1 = rect(0, 0, 22, 16)
r2 = rect(5, 5, 82, 57)

print(len(r1 | r2)) #объединение
print(len(r1 & r2)) #пересечение

per = r1 & r2

max_coord = max(per) #(x, y)
min_coord = min(per)

razn_x = max_coord[0] - min_coord[0]
razn_y = max_coord[1] - min_coord[1]

print(razn_x * razn_y)

count = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y < -x and y < x and y > x - 11 * 2 ** .5 and y > -x - 11 * 2 ** .5:
            count += 1
print(count)

print(sum(1 for x in range(-1000, 1000) for y in range(-1000, 1000) if y < -x and y < x and y > x - 11 * 2 ** .5 and y > -x - 11 * 2 ** .5))


count = 0

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y <= 16 and y >= 5 and x <= 22 and x >= 5:
            count += 1
print(count)
