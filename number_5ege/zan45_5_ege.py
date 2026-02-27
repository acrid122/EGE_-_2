# < 10 СС

def f_under10(x, a):
    s = ''
    while x > 0:
        s = str(x % a) + s
        x //= a
    return s

print(f_under10(7, 2))

def rec_f_under10(x, a):
    return '' if x == 0 else rec_f_under10(x // a, a) + str(x % a)

print(rec_f_under10(7, 2))


import string

print(string.printable)

def f_upper10(x, a):
    s = ''
    while x > 0:
        s = string.printable[x % a] + s
        x //= a
    return s

print(f_upper10(99, 25))

def rec_f_upper10(x, a):
    return '' if x == 0 else rec_f_under10(x // a, a) + string.printable[x % a]

print(rec_f_upper10(99, 25))


mas = []

for n in range(2, 1000):
    str_n = str(n)
    s1 = sum(map(lambda x: int(x) if int(x) % 2 == 0 else 0, str_n))
    #s1 = sum([i for i in str_n if int(i) % 2 == 0])
    s2 = sum(map(int, str_n[1::2]))
    #s2 = sum([i for i in str_n[1::2]])

    r = abs(s2 - s1)
    if r == 9:
        mas.append(n)

print(min(mas))


def f(x, a):
    return '' if x == 0 else f(x // a, a) + str(x % a)


mas = []

for n in range(1, 1000):
    n_5 = f(n, 5)
    if int(n_5[-1]) % 2 == 0:
        n_5 += '2'
    else:
        n_5 = '2' + n_5 + '3'
    
    r = int(n_5, 5)
    if r < 1000:
        mas.append(n)


print(max(mas))


'''
s = '123456789' #12, 23, 34, 45, 56, 67, 78, 89
s[1:] = '23456789'

zip(s, s[1:]) -> ('1', '2'), ('2', '3'), ('3', '4') ...
'''

mas = []


for n in range(10, 1000):
    str_n = str(n)
    pairs = list(map(lambda x: int(''.join(x)), zip(str_n, str_n[1:])))
    max_p, min_p = max(pairs), min(pairs)
    r = max_p + min_p
    if r == 137:
        mas.append(n)

print(min(mas))


def f(x, a):
    return '' if x == 0 else f(x // a, a) + str(x % a)

mas = []

for n in range(1, 10000):
    n_9 = f(n, 9)
    for _ in range(5):
        if n_9.count('5') == n_9.count('7'):
            n_9 += n_9[-1]
        else:
            n_9 += sorted(n_9, key = lambda x: n_9.count(x))[-1]
    r = hex(int(n_9, 9))
    if 'bac' in r:
        mas.append(n)

print(max(mas))


from collections import Counter

s = '123123412423143712573217681263781234'

#print(sorted(Counter(s), key = lambda x: ))


mas = []

for n in range(1, 1000):
    n_2 = bin(n)[2:]
    if n % 2 == 0:
        n_2 = n_2.replace('0', '2').replace('1', '0').replace('2', '1')
    else:
        n_2 = '1' + n_2[1:].replace('1', '00')
    r = int(n_2, 2)

    if r < 600:
        mas.append((r, n))


mas.sort(reverse = True)
print(mas[:10])
#print(bin(25)[2:], bin(~25))