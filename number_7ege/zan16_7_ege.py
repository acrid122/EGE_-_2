#ceil - функция, которая округляет результат в большую сторону
#int(), //, , floor из math - округление в меньшую сторону
#log2 - функция, которая берет логарифм по основанию два


from math import ceil, log2
#from math import *

N = 10000
print(ceil(log2(N)))

for t in range(10 ** 5, 0, -1):
    V_frame = 1920 * 1080 * 16
    V_frame_second = V_frame * 20
    V_audio = 2 * 44000 * 16 * t
    if (V_audio + V_frame_second * t) <= 3123 * 2 ** 23:
        print(t)
        break

for n in range(1, 1000):
    if 512 % n == 52:
        print(n)
        break

N = 65536
i = ceil(log2(N))
V = 1920 * 1080 * i
print(ceil(n * V / 2 ** 23))

N = 65536
i = ceil(log2(N))
j = i
for n in range(10 ** 5, 0, -1):
    V = 3840 * 2160 * (i + j)
    if V * n <= 8 * 2 ** 33:
        break
total = n * 2 + 45
print(ceil(total / 10))


N = 10 ** 7
i = ceil(log2(N))
for k in range (10 ** 7, 0, -1):
    V = k * i
    Vp = 10 * V
    U = 2.1 * 10 ** 6
    if Vp / U <= 3 * 60:
        print(k)
        break