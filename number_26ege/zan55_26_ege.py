with open('26_27779 (2).txt') as f:
    N = int(f.readline())
    sp = list(map(int, f))

sp.sort(reverse = True)

count, tmp_cookie = 1, sp[0]

for cookie in sp:
    if tmp_cookie - cookie >= 8:
        count += 1
        tmp_cookie = cookie

print(count, tmp_cookie)

with open('26_27636 (2).txt') as f:
    S, N = map(int, f.readline().split())
    sp = list(map(int, f))

sp.sort()

summa, count = 0, 0

for cont in sp:
    if summa + cont <= S:
        summa += cont
        count += 1

print(N - count, sum(sp) - summa)

with open('26_25363 (3).txt') as f:
    N = int(f.readline())
    sp = tuple(tuple(map(int, line.split())) for line in f)

'''
(
(800, 120)
(150, 200)
...
)
'''

new_sp = [(num, 1, x) if x < y else (num, 2, y) for num, (x, y) in enumerate(sp, 1)]

new_sp.sort(key = lambda x: x[2])

end = N + 1
for elem in new_sp:
    if elem[1] == 2:
        end -= 1 #997 - 1 = 996, 996 - 1 = 995

#end - под каким номером будет последний второй режим

print(new_sp[-1][0], N - end)

with open('26_23283 (1).txt') as f:
    K = int(f.readline())
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)

sp.sort()

windows = [0] * K #список из тысячи окон
#под каждым элементом windows будем хранить время освобождения

count, maxs = 0, 0

for start, end in sp:
    for i in range(K):
        if windows[i] <= start:
            windows[i] = end + 1
            count += 1
            maxs = i + 1
            break

print(count, maxs)

with open('26_24897 (2).txt') as f:
    N = int(f.readline())
    sp = list(tuple(map(int, line.split())) for line in f)

sp.sort(key = lambda x: (x[1], x[2], x[0]))

'''
[
[3213, 0, 445345, 0, 389213, 3213, 321312]
[0, 0, 0, 3123, 3213, 312321, 3123]
[0, 1, 0, 123, 312, 3434, 54241]
]
'''

new_sp = [[10**10 for _ in range(10 ** 4)] for _ in range(10 ** 4)]

for elem in sp:
    id_d, house, pod = elem
    new_sp[house][pod] = min(id_d, new_sp[house][pod])

max_c = [(0, float('inf'))] * 10 ** 4

for elem in new_sp:
    count = 1
    for i in range(len(elem)):
        if elem[i] != 10 ** 10:
            j = i + 1
            while j < len(elem) and elem[j] != 10 ** 10:
                count += 1
                j += 1
            if max_c[count] == 0:
                max_c[count] = (new_sp.index(elem), elem[i], i)
            else:
                if max_c[count][1] > elem[i]:
                    max_c[count] = (new_sp.index(elem), elem[i], i)
            count = 1

for elem in reversed(max_c):
    if elem[0] != 0:
        print(elem)
        break
'''              
[(0, inf), (778, 11, 707), (781, 40, 641), (478, 756, 608), (941, 1103, 282), 
 (77, 946, 597), (580, 26322, 9), (503, 518996, 805), (0, inf), (0, inf)]
'''
                


