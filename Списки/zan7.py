'''
Вложенные списки - это списки, содержащие другие списки в качестве элементов.

[[1, 2], [3, 4], [5, 6]] - двумерный список (матрица)

_ 0 1
0 1 2
1 3 4
2 5 6
'''

'''
copy() - поверхностная копия
deepcopy() - глубокая копия
'''
b = [[1, 2], [3, 4], [5, 6]]
c = b.copy()
c[0][0] = 9
print(b)

import copy
d = copy.deepcopy(b)
d[0][0] = 1
print(b, d)

#Матрица 3x3 с нулями
'''
[
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
]
'''

matrix = [[0] * 3 for _ in range(3)]
print(matrix)
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)
matrix = [[0] * 3] * 3 #все подписки ссылаются на один и тот же объект
matrix[0][0] = 2
print(matrix)

#b = [[1, 2], [3, 4], [5, 6]]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix = [[i * 2 for i in row] for row in matrix]
print(matrix)

tr = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9], 
        [10, 11, 12]
    ]
]
tr = [[[i * 2 for i in row2] for row2 in row1] for row1 in tr]
print(tr)

#развернуть список 2d в 1d
matrix = [i for row in matrix for i in row]
print(matrix)
#развернуть список 3d в 2d
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

tr = [row2 for row1 in tr for row2 in row1]
print(tr)

tr = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9], 
        [10, 11, 12]
    ]
]

tr1 = []
for row1 in tr:
    for row2 in row1:
        tr1.append(row2)
print(tr1)


numbers = [[1, 2], [3, 4], [5, 6]]
numbers.sort(key = sum, reverse = True)
print(numbers)

numbers = [[1, 2, 4], [3, 4, 5, 6], [5, 6]]
numbers.sort(key = len, reverse = True)
print(numbers)

numbers = [[1, 2, 4], [3, 4, 5, 6], [5, 6]]
numbers.sort(key = max, reverse = True)            
print(numbers)

words = ["cat", "dog"]
print(list(map(str.upper, words)))
            
words = ["cat", "dog"]
print(list(map(str.capitalize, words)))

#cat, i love you -> Cat I Love You; Cat, i love you

numbers = ['HH', '2D', '3F', '4I']
numbers.sort(key = lambda x: int(x, 20))
print(numbers)

numbers = [[1, 2], [3, 4], [5, 6], [1, -3], [0, 2]]
numbers.sort(key = lambda x: (x[0], -x[1]))
print(numbers)

#[1, 2], [1, -3]. [1, 2] -> (1, -2), [1, -3] -> (1, 3)

numbers = [[1, 2], [3, 4], [5, 6], [1, -3], [0, 2]]
numbers.sort(key = lambda x: (x[1], -x[0]))
print(numbers)

numbers = [
    [1, -1, 3],
    [1, 9, 2],
    [0, 15, 3],
    [4, 2, 5],
    [5, 6, 7]
]
numbers.sort(key = lambda x: (-x[2], x[1], -x[0]))
print(numbers)


numbers = [
    [
        [1, -1, 3],
        [1, 9, 2],
        [0, 15, 3]
    ],
    [
        [4, 2, 5],
        [5, 6, 7]
    ]
]
for row in numbers:
    row.sort(key = lambda x: (-x[2], x[1], -x[0]))
print(numbers)

numbers = [i ** 2 if i % 4 == 0 else i for i in range(1, 20)]

numbers = [i ** 3 if i > 10 else i ** 2 for i in range(1, 20)]

numbers = ['12', '13', '15']

numbers = [int(x) for x in numbers if int(x) % 3 == 0]
print(numbers)

numbers = [x for x in map(int, numbers) if x % 3 == 0]
print(numbers)
