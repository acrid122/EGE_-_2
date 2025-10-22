'''
== - эквиваленция (тройное равно, <->)

a == b = F
0 == 0 = 1
1 == 0 = 0
0 == 1 = 0
1 == 1 = 1

<= - импликация (->)

a <= b = F
0 <= 0 = 1
1 <= 0 = 0
0 <= 1 = 1
1 <= 1 = 1
not a or b = F
not 0 or 0 = 1
not 1 or 0 = 0
not 0 or 1 = 1
not 1 or 1 = 1

!= - исключающее или

a != b = F
0 != 0 = 0
1 != 0 = 1
0 != 1 = 1
1 != 1 = 0

(a and not b) or (not a and b) = 0
(a and not b) or (not a and b) = 1
...

(),
==, !=, <=
not
and
or
'''
print(not 5 <= 6)
print(not 5)
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (x or y) and not(y == z) and not w:
                    print(x, y, w, z)

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(((x or y) <= z) or (y == w) or z):
                    print(x, y, w, z)

