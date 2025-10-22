"""sp = []
for n in range(1, 10 ** 4):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_n += bin_n[-3:]
    else:
        bin_n += bin(n % 3 * 3)[2:]
    r = int(bin_n, 2)
    if r < 130:
        sp.append(n)

print(max(sp))"""

import string

def f7(n):
    sd = string.digits
    s = ""
    while n:
        s += sd[n % 7]
        n //= 7
    return s[::-1]

sp  = []

for n in range(1, 10 ** 4):
    s = ''
    if sum(map(int, f7(n))) % 2 == 0:
        s += "555"
    else: 
        s = "333" + s + "6"
    
    r = int(s, 7)
    if r < 12717:
        sp.append(n)
    
print(max(sp))
        


        

    