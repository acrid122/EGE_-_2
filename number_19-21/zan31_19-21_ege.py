from functools import cache

@cache
def f(x, m):
    #x - количество камней в куче
    #m - количество ходов в игре
    #Ванины ходы четные, а Петины - нечетные
    if x >= 125:
        return m % 2 == 0 #тут осуществляется проверка на четность.
        #В 19 задаче все Ванины ходы будут четные
    if m == 0:
        '''
        Если верхнее условие не сработало, то вернется 0, так как
        за нужное количество ходов не набралась сумма
        '''
        return 0
    #Формирование списка ходов
    sp = [f(x + 2, m - 1), f(x + 4, m - 1), f(x * 2, m - 1)]
    '''
    Вычитаю 1, так как только что был сделан ход
    '''
    return any(sp)


print(19, min([x for x in range(1, 125) if f(x, 2)]))
print(20, [x for x in range(1, 125) if f(x, 3) and not f(x, 1)])
print(21, [x for x in range(1, 125) if f(x, 4) and not f(x, 2)])

@cache
def f1(x, y, m):
    if x * y >= 541:
        return m % 2 == 0
    if m == 0:
        return 0
    sp = [f1(x + 10, y, m - 1), f1(x * 2, y, m - 1), 
          f1(x, y + 10, m - 1), f1(x, y * 2, m - 1)]
    return any(sp)

print(19, [i for i in range(1, 91) if f1(i, 6, 2)])