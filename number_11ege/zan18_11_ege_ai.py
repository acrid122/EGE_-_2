from math import ceil, log2
# for x in range(1, 10**5):
#     i = ceil(log2(10 + 15))
#     v = ceil(x * i /8)
#     if 947 * v > 6 * 2 ** 10:
#         print(x)
#         break
# for x in range(10**4, 1, -1):
#     i1 = ceil(log2(26))
#     v1 = 10 * i1 
#     i2 = ceil(log2(99999 - 1 + 1))
#     v2 = i2
#     dop = 13 
#     v = ceil((v1 + v2)/8) + dop
#     if v * x <= 1800:
#         print(x)
#         break
# for x in range(1, 10 ** 4):
#     i = ceil(log2(10 + 27))
#     v = ceil(x * i /8)
#     if 3548 * v > 12 * 2 ** 10:
#         print(x)
#         break

# for sd in range(1, 10**4):
#     i = ceil(log2(1020 + 10))
#     v = ceil(156 * i / 8)
#     if 7168 * v <= sd * 2 ** 10:
#         print(sd)
#         break

# for n in range(10 ** 5, 0, -1):
#     i = ceil(log2(n))
#     v = ceil( 257 * i /8)
#     if 295_740 * v <= 33 * 2 ** 20:
#         print(n)
#         break

# for dop in range(10 ** 4, 1, -1):
#     i = ceil(log2(10 + 52 + 70))
#     v = ceil(18 * i/8)
#     if 2000 * (v + dop) <= 100 * 2 ** 10:
#         print(dop)
#         break

# for x in range(10 ** 8, 0, -1):
#     i = ceil(log2(26 + 32724))
#     v = ceil(223 * i / 8)
#     if x * v <= 17 * 2 ** 30:
#         print(x)
#         break


# i1 = ceil(log2(52 + 10))
# v1 = ceil(i1 * 12 / 8)
# i2 = ceil(log2(1000 - 1 + 1))
# v2 = ceil(i2 * 1 / 8)
# dop = 60 
# print(v1 + v2 + dop)

# for x in range(10 ** 5, 0, -1):
#     i = ceil(log2(10 + 26 + 476))
#     v = ceil(x * i / 8)
#     if v * 5000 <= 1 * 2 ** 20:
#         print(x)
#         break

# for dop in range(1, 10 ** 4):
#     i = ceil(log2(10 + 510))
#     v = ceil(99 * i / 8 )
#     if 4322 * (v + dop) >= 543 * 2 ** 10:
#         print(dop)
#         break  

# for x in range(10 ** 4, 0 , -1):
#     i = ceil(log2(52 + 10 + 963))
#     v = ceil(x * i / 8)
#     if 2000 * v  <= 693 * 2 ** 10:
#         print(x)
#         break

# for  x in range(1, 10 ** 4):
#     i = ceil(log2(10 + 26 + 450))
#     v = ceil(x * i / 8)
#     if 708 * v >= 213 * 2 ** 10:
#         print(x)
#         break


# i = ceil(log2(10 + 4080))
# v =ceil(79 * i / 8)
# print(ceil(65_536 * v / 2 ** 10))

i1  = ceil(log2(26))
v1 = 20 * i1
i2 = ceil(log2(3000 - 1 + 1))
v2 = 1 * i2
v = ceil((v1 + v2)/8)
print(2500 / 50 - v)