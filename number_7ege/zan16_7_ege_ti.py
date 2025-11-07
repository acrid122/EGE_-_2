from math import ceil, log2
N = 65536
i = ceil(log2(N))
for n in range(10 ** 7, 0, -1):
    v = 3840 * 2160 * i
    if v * n <= 16 * 2 ** 33:
        break
print(14 * n + 722)




N = 256
i = ceil(log2(N))
for n in range(10 ** 7, 0, -1):
    v = 1280 * 1024 * i
    if v * n <= 4 * 2 ** 33:
        break
print(34 * n + 307)




N = 256
i = ceil(log2(N))
v = 1280 * 1024 * i
for n in range(10 ** 7, 0, -1):
    if v * n <= 4 * 2 ** 33:
        break
print(8921742524 % n)





N = 4096
i = ceil(log2(N))
v = 1536 * 1024 * i
v_p = v * 150
for k in range(100, 0, -1):
    if k / 100 * v_p / (288 * 2 ** 13) <= 4 * 60:
        break
print(100 - k)





N = 65536
i = ceil(log2(N))
v = 1280 * 800 * i
for n in range(1, 10 ** 5):
    if 0.6 * v / (300 * 2 ** 13) <= n:
        print(n)
        break




v_v = 1920 * 1080 * 8 * 60 * 60
v_s = 2 * 24000 * 6 * 60
v_0 = (v_s + v_v) * 50
print(ceil(v_0 / (2 ** 13)))






