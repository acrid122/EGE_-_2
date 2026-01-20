with open("17_23905.txt") as f:
    sp = list(map(int, f))
count, summ = 0, 0
maxx = max(i for i in sp if i % 100 == 37)
for i in range(len(sp) - 4):
    s = sp[i : i + 4]
    if sum(1 for j in s if j > maxx) == 2 and sum(1 for j in s if j % 10 == j // 10 % 10) == 1:
        count += 1
        summ += sum(j for j in s if j % 10 == j // 10 % 10)
print(count, summ)


with open("17_23563.txt") as f:
    sp = list(map(int, f))
count, summ = 0, float('-inf') 
minn = min(i for i in sp if i % 35 == 0 and i > 0)
for i in range(len(sp) - 2):
    s = sp[i : i + 2]
    if s[0] != s[1] and abs(s[0] - s[1]) % minn == 0:
        count += 1
        summ = max(summ, sum(s))
print(count, summ)



with open("17_17636.txt") as f:
    sp = list(map(int, f))
count, summ = 0, 0
for i in range(len(sp) - 3):
    s = sp[i : i + 3]
    