from statistics import mean
with open("9_6.txt") as f:
    res, number = 0, 0
    for i in f:
        s = list(map(int, i.split()))
        number += 1
        povt = [i for i in s if s.count(i) != 1]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) > 0 and len(nepovt) > 0 and sum(s) % 2 != 0 and sum(povt) ** 2 > sum(nepovt) ** 2:
            res = number
print(res)



with open("9_7.txt") as f:
    for i in f:
        s = list(map(int, i.split()))
        s.sort()
        max2 = s[-2]
        summ = [elem for elem in s if elem < 90]
        if max2 ** 2 > (max(s) * min(s)) and sum(s) % 2 == 0 and abs(sum(summ) % 10) == 4:
            print(sum(s))
            break
        
with open("9_8.txt") as f:
    for i in f:
        summo = 0
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) > 1]
        chet = [i for i in s if i % 2 == 0]
        nechet = [i ** 3 for i in s if i % 2 != 0]
        if len(povt) == 0 and sum(chet) ** 2 > sum(nechet):
            summo = sum(s)
print(summo)




with open("9_9.txt") as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) == 3]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) == 3 and nepovt[0] % 2 == 0 and povt[0] % 2 != 0:
            count+=1
print(count)
1 24 