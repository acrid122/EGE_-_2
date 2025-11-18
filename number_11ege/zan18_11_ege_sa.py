from math import *
'''N = 15 + 10
i = ceil(log2(N))
for k in range(1, 10 ** 5):
    V = ceil(i * k / 8)
    if V * 947 > 6 * 2 ** 10:
        print(k)
        break
N1 = 26
i1 = ceil(log2(N1))
k1 = 10
N2 = 99999
i2 = ceil(log2(N2))
V = ceil((i1 * k1 + i2) / 8)
for x in range(10 ** 5, 1, -1):
    if (V + 13) * x <= 1800:
        print(x)
        break

for k in range(1, 10 ** 5):
    N = 27
    i = ceil(log2(N))
    V = ceil(i * k / 8)
    if V * 3548 > 12 * 2 ** 10:
        print(k)
        break

N = 10 + 1020
i = ceil(log2(N))
k = 156
V = ceil(k * i / 8)
res = ceil(7168 * V / 2 ** 10)
print(res)

k = 257
for N in range(10 ** 5, 1, -1):
    i = ceil(log2(N))
    V = ceil(i * k / 8)
    if 295740 * V <= 33 * 2 ** 20:
        print(N)
        break


k = 18
N = 10 + 52 + 70
i = ceil(log2(N))
V = ceil(i * k / 8)
for x in range(10 ** 5, 1, -1):
    if (V + x) * 2000 <= 100 * 2 ** 10:
        print(x)
        break
    
k = 223
N = 10 + 26 + 32724
i = ceil(log2(N))
V = ceil(i * k / 8)
for x in range(10 ** 8, 1, -1):
    if V * x <= 17 * 2 ** 30:
        print(x)
        break 
'''

k = 12
N = 52 + 10
i = ceil(log2(N))
N1 = 1000
i1 = ceil(log2(N1))
V = ceil(k * i / 8) + ceil(i1 / 8) + 60
print(V)

N = 10 + 26 + 476
i = ceil(log2(N))
for k in range(10 ** 5, 1, -1):
    V = ceil(k * i / 8)
    if V * 5000 <= 2 ** 20:
        print(k)
        break

k = 99
N = 10 + 510
i = ceil(log2(N))
V = ceil(i * k / 8)
for x in range(1, 10 ** 5):
    if (V + x) * 4322 > 543 * 2 ** 10:
        print(x)
        break
    
N = 52 + 963 + 10
i = ceil(log2(N))
for k in range(10 ** 5, 1, -1):
    V = ceil(i * k / 8)
    if 2000 * V <= 693 * 2 ** 10:
        print(k)
        break

N = 26 + 10 + 450
i = ceil(log2(N))
for k in range(1, 10 ** 5):
    V = ceil(k * i / 8)
    if 708 * V > 213 * 2 ** 10:
        print(k)
        break
    
N = 10 + 4080
i = ceil(log2(N))
k = 79
V = ceil(i * k / 8)
print(ceil(V * 65536 / 2 ** 10))

N = 26
i = ceil(log2(N))
N1 = 3000
i1 = ceil(log2(N))
for x in range(1, 10 ** 5):
    V = ceil(i * k / 8) + ceil(i1 / 8) + x
    if V * 50 == 2500:
        print(x)
        break