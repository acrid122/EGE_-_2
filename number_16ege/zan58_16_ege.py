from functools import *

@lru_cache(maxsize = 50) #@cache #
def f(n):
    return 3 if n < 10 else (n + 4) * f(n - 5)

for n in range(257500):
    f(n)

print((f(257487) // 683 + 67 * f(257477)) // f(257472))
#segmentation fault

#24994270044009
#RecursionError: maximum recursion depth exceeded

""" sp = []

for n in range(257500):
    if n < 10:
        sp.append(3)
    else:
        sp.append((n + 4) * sp[n - 5])
print((sp[257487] // 683 + 67 * sp[257477]) // sp[257472]) """

sp = []
for n in range(2, 258000, 5):
    if n < 10:
        sp.append(3)
    else:
        sp.append((n + 4) * sp[-1])

print((sp[257487 // 5] // 683 + 67 * sp[257477 // 5]) // sp[257472 // 5])

""" sp2 = [0] * 257500
#Memory Error

for n in range(257500):
    if n < 10:
        sp2[n] = 3
    else:
        sp2[n] = (n + 4) * sp2[n - 5]
print((sp2[257487] // 683 + 67 * sp2[257477]) // sp2[257472]) """

""" sp2 = [0] * 255_750_000_000
print(sp2) """

from fractions import Fraction

@cache
#@lru_cache(maxsize = 10)
def f1(n):
    if n >= 19:
        return f1(n - 4) + 3580
    else:
        return 6 * (g1(n - 7) - 36)

@cache
#@lru_cache(maxsize = 100)
def g1(n):
    if n >= 248045:
        return n / 20 + 28
    else:
        return g1(n + 9) - 4

for n in range(248100, -1, -1):
    g1(n)

for n in range(674000):
    f1(n)

print(f1(673990) + f1(673980))
#RecursionError: maximum recursion depth exceeded
@lru_cache(maxsize = 311_000)
def g2(n):
    if n < 28:
        return 3 * n - 4
    return g2(n - 5) - 15

@lru_cache(maxsize = 311_000)
def f2(n):
    if n < 31054:
        return f2(n + 4) + 3020
    return 3 * (g2(n - 2) - 15)

for n in range(311_000):
    g2(n)
for n in range(311_000, -1, -1):
    f2(n)
print(f2(15))

@cache
def q3(n):
    if n < 21:
        return n + 4
    return q3(n - 4) + 2
@cache
def g3(n):
    if n >= 11240:
        return q3(n)
    return g3(n + 3) + 2
@cache
def f3(n):
    if n < 43:
        return g3(n + 4)
    return 2 * f3(n - 2) - f3(n - 4) + 2
for n in range(12_000):
    q3(n)
for n in range(12_000, -1, -1):
    g3(n)
for n in range(12_000):
    f3(n)
print(f3(2026))


from sys import getsizeof
print(getsizeof(f(257487))) #113540
print(113540 * 257487 / 2 ** 30)