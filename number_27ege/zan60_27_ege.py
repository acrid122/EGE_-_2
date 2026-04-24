from math import *

def clusterize(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neigbours = {p for p in data if dist(point, p) <= eps}
            cluster.extend(neigbours)
            data -= neigbours
        if len(cluster) > 10:
            diameter = 0
            d_point = [float('-inf'), float('-inf')]
            for i in range(len(cluster)):
                for j in range(i + 1, len(cluster)):
                    if diameter <= dist(cluster[i], cluster[j]):
                        diameter = dist(cluster[i], cluster[j])
                        d_point[0], d_point[1] = cluster[i], cluster[j]
            clusters.append((cluster, d_point))
    return clusters

clustersA = clusterize('27A_27591.txt', 1)
print(len(clustersA))
Px = float('inf')
for _, d_point in clustersA:
    Px = min(Px, d_point[0][0] + d_point[1][0])

Py = float('-inf')
for _, d_point in clustersA:
    Py = max(Py, d_point[0][1] + d_point[1][1])
print(int(Px * 10000), int(Py * 10000))
    
clustersB = clusterize('27B_27591.txt', 1)
print(len(clustersB))
clustersB.sort(key = lambda cluster: len(cluster[0]))

min_clusterB_d = clustersB[0][1]
print(min_clusterB_d)
print(int(dist(min_clusterB_d[0], min_clusterB_d[1]) * 10000))

Q2 = 0
for _, d_point in clustersB:
    for _, n_d_point in clustersB:
        Q2 = max(Q2, dist(d_point[0], n_d_point[0]),
                 dist(d_point[0], n_d_point[1]), 
                 dist(d_point[1], n_d_point[0]), 
                 dist(d_point[1], n_d_point[1]))
print(int(Q2 * 10000))


def clusterize1(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neigbours = {p for p in data if dist(point, p) <= eps}
            cluster.extend(neigbours)
            data -= neigbours
        if len(cluster) > 10:
            anti_center = max(cluster, key = lambda p: sum(dist(p, p1) for p1 in cluster))
            clusters.append((cluster, anti_center))
    return clusters

clustersA = clusterize1('27A_27590.txt', 1)
clustersA.sort(key = lambda cluster: len(cluster[0]))
Px = clustersA[0][1][0] + clustersA[0][1][1]
Py = clustersA[1][1][0] + clustersA[1][1][1]
print(int(Px * 10000), int(Py * 10000))

clustersB = clusterize1('27B_27590.txt', 1)
print(len(clustersB))
Q1 = 0
max_dist = 0
for _, anti_center in clustersB:
    if max_dist <= dist(anti_center, (0, 0)):
        max_dist = dist(anti_center, (0, 0))
        Q1 = anti_center[0]

Q2 = 0
min_dist = float('inf')
for _, anti_center in clustersB:
    if min_dist >= dist(anti_center, (0, 0)):
        min_dist = dist(anti_center, (0, 0))
        Q2 = anti_center[1]
print(int(Q1 * 10000), int(Q2 * 10000))


def clusterize2(data, R):
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neigbours = {p for p in data if dist(point, p) < R}
            cluster.extend(neigbours)
            data -= neigbours
        anti_center = max(cluster, key = lambda p: sum(dist(p, p1) for p1 in cluster))
        clusters.append((cluster, anti_center))
    return clusters

with open('27A_22076.txt') as f:
    R = float(f.readline())
    data = {tuple(map(float, line.split())) for line in f}
    c_data = {elem for elem in data}

clustersA = clusterize2(data, R)
anti_center = max(c_data, key = lambda point: 
                  sum(dist(point, n_anti_center) for _, n_anti_center in clustersA))
x, y = anti_center
print(int(x * 10000), int(y * 10000))

with open('27B_22076.txt') as f:
    R = float(f.readline())
    data = {tuple(map(float, line.split())) for line in f}
    c_data = {elem for elem in data}

clustersA = clusterize2(data, R)
anti_center = max(c_data, key = lambda point: 
                  sum(dist(point, n_anti_center) for _, n_anti_center in clustersA))
x, y = anti_center
print(abs(int(x * 10000)), abs(int(y * 10000)))