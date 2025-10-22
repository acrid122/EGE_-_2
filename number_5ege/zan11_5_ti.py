

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

















import string

def f7(number):
    s = ''
    s1 = string.digits + string.ascii_lowercase
    while number > 0:
        s += s1[number % 7]
        number //= 7
    return s[::-1]
sp = []
for n in range(1, 10 ** 4):
    ronaldo = f7(n)
    '''
    ValueError: invalid literal for int() with base 10: 'b'
    '''
    if sum(map(int, ronaldo)) % 2 == 0:
        ronaldo += '555'
    else:
        ronaldo = '33' + ronaldo + '6'
    r = int(ronaldo, 7)
    if r < 12717:
        sp.append(n)
print(max(sp))
    

