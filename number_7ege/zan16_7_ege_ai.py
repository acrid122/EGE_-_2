from math import *
v = 3840 * 2160 * ceil(log2(65536))
sd = 16 * 2 ** 33
print(14 * floor(sd/v) + 722)


v = 1280 * 1024 * ceil(log2(256))
sd = 4 * 2 ** 33
print(34 * floor(sd/v) + 307)

for k in range(10**7 , 1, -1):
    v = 1280 * 1024 * ceil(log2(256))
    sd = 4 * 2 ** 33
    if v * k <= sd:
        print(8921742524 % k)
        break
for x in range(0, 100):
    v = 1536 * 1024 * ceil(log2(4096))
    n = 150 
    u = 288 * 2 ** 13
    t = 4 * 60
    if v * n * (100 - x)/100 <= u * t:
        print(x)
        break
print((4*16*0.4)/(2*0.6))
for n in range(1, 10**4):
    img = 1200 * 800 * ceil(log2(65536)) 
    u = 300 * 2 ** 13
    k = 0.6
    if img * k <= u * n:
        print(n)
        break



