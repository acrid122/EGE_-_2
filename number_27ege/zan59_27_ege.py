from math import *

def clusterize(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)} #считывание точек из файла в множество. до этого необходимо в файле заменить все , на точки
    clusters = [] #список кластеров, который будет выглядеть так: [(список_точек_кластера, медоид), ()]
    while data: #пока множество точек в data непустое
        cluster = [data.pop()] #удаляю точку из data и на основе этой точки создаю кластер
        for point in cluster: #прохожусь по точкам и ищу соседей
            neighbours = {n_point for n_point in data if dist(point, n_point) <= eps} #ищу соседей
            '''
            cluster = [(1, 1)]
            neighbours = {(1, 2), (2, 1)}
            cluster = [(1, 1), (1, 2), (2, 1), (), (), (), ()]
            '''
            cluster.extend(neighbours) #расширяю список точек новыми соседями (они лежат в одном кластере)
            data -= neighbours #убираю из data множество соседей текущей точки, так как эти точки не могут лежать в другом кластере
        medoid = min(cluster, key = lambda point: sum(dist(point, n_point) for n_point in cluster))
        clusters.append((cluster, medoid))
    return clusters


clustersA = clusterize('27A_27780 (3).txt', 1)
print(len(clustersA))
A1 = len(max(clustersA, key = lambda cluster: len(cluster[0]))[0])
A2 = sum(dist((1.0, 1.5), medoid) for _, medoid in clustersA)
print(A1, int(A2 * 10000))

clustersB = clusterize('27B_27780.txt', 2)
clustersB.sort(key = lambda cluster: len(cluster[0]))
print(len(clustersB))
B1 = sum(1 for point in clustersB[1][0] if dist(point, clustersB[1][1]) <= 1.2 and point != clustersB[1][1])
B2 = float('inf')
for point in clustersB[2][0]:
    if point != clustersB[2][1]:
        B2 = min(B2, dist(point, clustersB[2][1]))
print(B1, int(B2 * 10000))


clustersA1 = clusterize('27A_27593.txt', 1)
Px = min(dist((5.5, 9.1), medoid) for _, medoid in clustersA1)
Py = dist((5.5, 9.1), ((clustersA1[1][1][0] + clustersA1[0][1][0]) / 2, (clustersA1[1][1][1] + clustersA1[0][1][1]) / 2))
#[([], (x, y)), ([], ()), ([], ()), ...]
print(int(Px * 10000), int(Py * 10000))