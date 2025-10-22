'''
int - integer (целые числа). Целочисленный тип данных. 10000000000000000000000000000000000000000000000000000000000000000
'''
x = 3.5
print(int(x)) #остается только целая часть

y = 3
print(float(y))

'''
float - число с плавающей точкой (вещественное число). Точность ограничена (около 15 знаков) из-за представления (двочное) в памяти.
'''

z = 3.5
z = 1.0
z = -0.5
z = 2.5e-3 #0.0025
z = .52
print(z)

print(0.1 + 0.2 == 0.3) #неточная точность, это связано со способом предстваления вещественных чисел в памяти.

import math

print(math.isclose(0.1 + 0.2, 0.3)) #"почти равенство" - меньше, чем погрешность

a = 0.1 + 0.2
b = 0.3
print(abs(b - a) < 1e-9)

from decimal import Decimal


a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)


from fractions import Fraction


a = Fraction(1, 10)
b = Fraction(2, 10)
print(a + b)

'''
complex (комплексные числа). Это числа с реальной и мнимой частями.
'''
z = 2 + 3j
print(type(z))
print(z.real, z.imag)

print(help(int)) #help - ф-ия, которая помогает вспомнить всю начинку класса/библиотеки
print(y.__add__(3)) #метод класса int
print((5).__add__(3)) #ставим скобки, так как интерпретатор ожидает десятичную часть числа после точки.

#Арифметические операции
'''
+ - сложение
- - вычитание
* - умножение
/ - деление
** - возведение в степень
// - целочисленное деление
% - остаток от деления
'''

#PEMDAS - приоритет арифметических операций
'''
P - Parentheses (скобки)
E - Exponents (возведение в степень)
M - Multiplication (умножение)
D - Divison (деление)
A - Addition (сложение)
S - Subtraction (вычитание)
'''
'''
1. ()
2. **
3. унарный +, - (-5, +7)
4. *, /, //, %
5. +, -
'''

import math #при таком импорте всегда припоисываем имя библиотеки перед используемой функций или классом
print(math.sqrt(6))
'''
from math import * #* - импорт абсолютно всей начинки
print(sqrt(6))

from math import sqrt, gcd, log #перечисление через запятую того функционала, который нужен

import matplotlib as mpl #сокращение названия модуля для более удобного использования
print(mpl.color_sequences())
'''

s = 'dasdasda'
s1 = "adasdad"
s2 = """
fsdfsd
ffsdfsd
f
sd"""

while True:
    try:
        num1 = int(input("Первое число: "))
        num2 = int(input("Второе число: "))
    except ValueError:
        print('Неверный ввод!')
        continue

    operation = input("Действие (+, -, *, /, //, %, **, sqrt, round of division (round), log, ln, sin, cos, fact)")

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("на 0 нельзя делить!")
    elif operation == "//":
        try:
            print(num1 // num2)
        except ZeroDivisionError:
            print("на 0 нельзя делить!")
    elif operation == "%":
        try:
            print(num1 % num2)
        except ZeroDivisionError:
            print("на 0 нельзя делить!")
    elif operation == "**":
        print(num1 ** num2)   
    elif operation == "sqrt":
        print(num1 ** (1 / num2))
    elif operation == "round":
       print(round(num1/num2))
    elif operation == "log":
        print(math.log(num1, num2))
    elif operation == "ln":
        print(math.log(num2, math.e))
    elif operation == "sin":
        print(math.sin(num2))
    elif operation == "cos":
        print(math.cos(num2))
    elif operation == "fact":
        try:
            print(math.factorial(num2))
        except ValueError:
            print("введи другое значение!")
    else:
        print('Неизвестное действие')

    if input('Продолжить? (да/нет): ') == "нет":
        break


'''
Остатки от отрицательных чисел
-7 % 3 = 2
7 % 3 = 1
3 - 1 = 2 - остаток от отрицательного числа
'''

'''
round() - математическое округление
'''
print(round(1.5)) #округление происходит в сторону четного числа, если оно равноудалено от двух целых
print(round(10.5))
print(round(10.51))
print(round(10.525, 2)) #второй параметр - округление до количества знаков

'''
divmod() - возвращает кортеж, содержащий частное и остаток
'''

print(divmod(7, 3))

'''
pow() - возведение в степень.
'''
print(pow(2, 3, 2))