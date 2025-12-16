from statistics import mean
'''with open("9_6.txt") as f:
    res, number = 0, 0
    for i in f:
        s = list(map(int, i.split()))
        number += 1
        povt = [i for i in s if s.count(i) > 1]
        nepovt = [i for i in s if s.count(i) == 1]
        if len(povt) > 0 and len(nepovt) > 0 and (sum(povt) ** 2 > sum(nepovt) ** 2) and sum(s) % 2 == 1:
            res = number
    print(res)'''
'''with open("9_7.txt") as f:
    for i in f:
        s = list(map(int, i.split()))
        s.sort()
        mensh90 = [i for i in s if i < 90]
        if s[-2] ** 2 > (s[0] * s[-1]) and (sum(s) %  2 == 0) and (sum(mensh90) % 10 == 4):
            print(sum(s))
            break'''
'''with open("9_8.txt") as f:
    for i in f:
        s = list(map(int, i.split()))
        povt = [i for i in s if s.count(i) > 1]
        chet = [i for i in s if i % 2 == 0]
        nechet = [i ** 3 for i in s if i % 2 == 1]
        if len(povt) == 0 and sum(chet) ** 2 > sum(nechet):
            summa = sum(s)
    print(summa)'''

with  open("9_9.txt") as f:
    count = 0
    for i in f:
        s = list(map(int, i.ssplit()))
        povt = [i for i in s in s.count(i) == 3]:
        nepovt 