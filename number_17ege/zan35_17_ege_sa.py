'''with open('17_23905.txt') as f:
    s = list(map(int, f))
summ = 0
count = 0
max_37 = max(i for i in s if i % 100 == 37)
for i in range(len(s) - 3):
    sp = s[i : i + 4]
    if sum(1 for j in sp if j > max_37) == 2 and sum(1 for j in sp if j % 10 == j // 10 % 10) == 1:
        count += 1
        summ += sum(j for j in sp if j % 10 == j // 10 % 10)
print(count, summ)'''

'''with open('17_23563.txt') as f:
    s = list(map(int, f))
count, summ = 0, float('-inf')
min_35 = min(i for i in s if i > 0 and abs(i) % 35 == 0)
for i in range(len(s) - 1):
    sp = s[i:i+2]
    if sp[0] != sp[1] and abs(sp[0] - sp[1]) % min_35 == 0:
        count += 1
        summ = max(summ, sum(sp))
print(count, summ)'''

