from math import *
N = 65536
i = ceil(log2(N))
V = 1200 * 800 * i
for n in range(1, 10 ** 5):
    if V * 0.6 <= 300 * 2 ** 13 * n:
           print(n)
           break