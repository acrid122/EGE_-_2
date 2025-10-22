'''
  2 3 4 5 6 7 8 9 10 11 12 ... 36
0 1 2 3 4 5 6 7 8 9  a  b  ... z
'''

'''
#Как перевести из 10 СС в 2СС
'''
print(bin(10)[2:])

'''
#Как перевести из 10 СС в 8СС
'''
print(oct(10)[2:])

'''
#Как перевести из 10 СС в 16СС
'''
print(hex(10)[2:]) #если в результате перевода в строке получаются буквы, то эти буквы в нижнем регистре, прописная - заглавная, строчная - маленькая
print('A' in hex(10)[2:]) #False, потому что в нижнем регистре

'''
Как перевести из 10СС в любую другую. Это не очень хороший код.
'''

def f(number, base):
    s = ''
    while number > 0:
        s += str(number % base)
        number //= base
    return s[::-1]

'''
120_10 -> X_24
s = ''
while 120 > 0:
    s += str(120 % 24) #0
    120 //= 24 #5

while 5 > 0:
    0 += str(5 % 24) #05
    5 //= 24 #0

while 0 > 0:
    False

s = '05'
s[::-1] = '50'
'''

print(f(7, 2))
print(f(10, 3))
print(f(120, 11))

import string
print(string.digits) #все цифры
print(string.ascii_lowercase) #все буквы


def f1(number, base):
    s = ''
    #s1 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % base]
        number //= base
    return s[::-1]

print(f1(7, 2))
print(f1(10, 3))
print(f1(120, 11))

'''
Как перевести из какой-то СС в 10.
'''

print(int('AA', 11)) #первый параметр - в формате строки. туда указываем, что переводить. а второй параметр - из какой системы счисления перевод
print(int(10.5))
print(int('10'))

sp = []
for n in range(1, 10 ** 4):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_n += bin_n[-3:]  
    else: 
        bin_n += bin((n % 3) * 3)[2:] #bin_n = 1000_2    10 -> bin_n = 10000b10
    r = int(bin_n, 2)
    if r >= 200:
        sp.append(n)
print(min(sp))

sp = []
for n in range(1, 10 ** 4):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = '10' + bin_n
    else:
        bin_n = '1' + bin_n + '01'
    r = int(bin_n, 2)
    if r < 30:
        sp.append(n)
print(max(sp))

def f2(number):
    s = ''
    s1 = string.digits + string.ascii_uppercase
    while number > 0:
        s += s1[number % 3]
        number //= 3
    return s[::-1]


sp = []
for n in range(1, 10 ** 4):
    tr_n = f2(n)
    if n % 3 == 0:
        tr_n = '1' + tr_n + '02'
    else:
        tr_n += f2((n % 3) * 4)
    r = int(tr_n, 3)
    if r < 100:
        sp.append(n)
print(max(sp))


#сумма цифр числа

p = 50

print(sum(map(int, str(p))))

