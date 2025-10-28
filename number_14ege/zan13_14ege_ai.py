import string 
for p in range(7, 37):
    ch1 = "2465123"
    ch2 = "251341"
    v = int(ch1, p)  + int(ch2, p)
    if v % 17 == 0:
        print(v // 17)
        break
        

s = 17 * 125 ** 453 + 117 * 5 ** 231 - 3 * 5 ** 13 - 2357
count = 0
while s:
    if s % 125 <= 37:
        count += 1
    s //= 125
print(count)

s = 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
count = 0
while s:
    if s % 49 <= 9:
        count += 1
    s //= 49
print(count)

s = string.digits + string.ascii_uppercase
for x in s[:29]:
    ch1 = f"463{x}7921"
    ch2 = f"8241{x}153"
    v = int(ch1, 29) + int(ch2, 29) 
    if v % 28 == 0:
        print(v//28)
        break

s = string.digits + string.ascii_uppercase
for x in s[:14]:
    ch1 = int(f"4B3{x}1", 14)
    ch2 = int(f"5{x}F83", 16)
    v = ch1 + ch2
    if v % 13 == 0:
        print(v // 13)
        break


s = string.digits + string.ascii_uppercase
for x in s[1:13]:
    ch1 = int(f"9{x}AB", 13)
    ch2 = int(f"{x}46C", 16)
    ch3 = int(f"B7{x}", 15)
    v = ch1 + ch2 - ch3 
    if v % 14 == 0:
        print(v // 14)
        break

s = string.digits + string.ascii_uppercase
for p in range(10, 37):
    for x in s[1:p]:
        for y in s[1:p]:
            ch1 = int(f"24{x}9", p)
            ch2 = int(f"{y}{x}{y}3", p)
            ch3 = int(f"{x}4{y}0", p)
            if ch1 + ch2 == ch3:   
                print(int(f"{x}{y}{y}", p))
                
