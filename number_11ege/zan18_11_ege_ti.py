from math import ceil, log2
for x in range(10 ** 5, 0, -1):
    i = ceil(log2(66 + x))
    v = ceil(21 * i / 8)
    if 1300 * v <= 25 * 2 ** 10:
        print(x)
        break