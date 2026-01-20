with open("17_23905.txt") as f:
    sp = list(map(int, f))
summa = 0
max_37 = max(i for i in sp if abs(i) % 100 == 37)
c = 0
for i in range(len(sp) - 3):
    s = sp[i : i + 4]
    if sum(1 for j in s if j % 10 == j // 10 % 10) == 1 and sum(1 for j in s if j > max_37) == 2:
        summa += sum(j for j in s if j % 10 == j // 10 % 10)
        c += 1

print(c, summa)