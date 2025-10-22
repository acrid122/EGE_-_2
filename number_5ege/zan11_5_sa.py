import string

sp = []
for n in range(1, 10 ** 4):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += bin((n % 3) * 3)[2:]
    r = int(bin_n, 2)
    if r < 130:
        sp.append(n)
print(max(sp))

def seven(number, base):
    s = ''
    s1 = string.digits
    while number > 0:
        s += s1[number % base]
        number //= base
    return s[::-1]


sp = []
for n in range(1, 10 ** 4):
    sev_n = seven(n, 7)
    if sum(map(int, sev_n)) % 2 == 0:
        sev_n += '555'
    else:
        sev_n = '33' + sev_n + '6'
    r = int(sev_n, 7)
    if r < 12717:
        sp.append(n)
print(max(sp))