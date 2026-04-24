#(x, y)
#((x, y), строка)

from math import *

def clusterize(file, eps):
    data = {(tuple(map(float, line.split()[:2])), line.split()[2]) 
            for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neighbours = {p for p in data if dist(point[0], p[0]) <= eps}
            cluster.extend(neighbours)
            data -= neighbours
        center = min(cluster, key = lambda point: 
                     sum(dist(point[0], p[0]) for p in cluster))
        clusters.append((cluster, center))
    return clusters
#27_29081
clustersA = clusterize('27_A_29081.txt', 1)
print(len(clustersA))

A1, A2 = float('inf'), float('-inf')
for cluster, center in clustersA: #[([], center), (), () ...]
    for point in cluster:
        if 'VII' in point[1]:
            A1 = min(A1, dist(point[0], center[0]))
            A2 = max(A2, dist(point[0], center[0]))
print(int(A1 * 10000), int(A2 * 10000))


clustersB = clusterize('27_B_29081.txt', 1)
print(len(clustersB))

star8 = [(point[0], center) for cluster, center in clustersB 
         for point in cluster if int(point[1][1]) >= 8]

B1 = float('inf')
B2 = []
for i in range(len(star8)):
    for j in range(i + 1, len(star8)):
        if star8[i][1] != star8[j][1]:
            B1 = min(B1, dist(star8[i][0], star8[j][0]))
        else:
            B2.append(dist(star8[i][0], star8[j][0]))
B2 = sum(B2) / len(B2)
print(int(B1 * 10000), int(B2 * 10000))
                
#27_29080
clustersA = clusterize('27_A_29080.txt', 1)
print(len(clustersA))

min_clustersA = min(clustersA, key = lambda cluster: len(cluster[0]))
max_clustersA = max(clustersA, key = lambda cluster: len(cluster[0]))

star_l3 = [point[0] for cluster, _ in clustersA
           for point in cluster if 'L3' in point[1]]

A1 = float('-inf')
A2 = float('-inf')
'''
clustersA = [([((x, y), строка), ((x, y), строка), ((x, y), строка)
], ((x, y), строка)), (), () ...]

[([], ((x, y), строка)), (), ...]

[(cluster, center), (cluster1, center1), () ...]
min_clustersA = (cluster, center) -> center = ((x, y), строка)
'''
for point in star_l3:
    A1 = max(A1, dist(point, min_clustersA[1][0]))
    A2 = max(A2, dist(point, max_clustersA[1][0]))
print(int(A1 * 10000), int(A2 * 10000))

clustersB = clusterize('27_B_29080.txt', 1)
print(len(clustersB))
s_clustersB = sorted(clustersB, key = lambda cluster:
                     sum(1 for point in cluster[0] if point[1][0] == 'L'))

B1 = dist(s_clustersB[0][1][0], s_clustersB[2][1][0])
print(int(B1 * 10000))

blue_stars = [point[0] for cluster, _ in clustersB
              for point in cluster if point[1][0] == 'L']

B2 = float('-inf')
for i in range(len(blue_stars)):
    for j in range(i + 1, len(blue_stars)):
        B2 = max(B2, dist(blue_stars[i], blue_stars[j]))
print(int(B2 * 10000))


def clusterize1(file, eps):
    data = {tuple(map(float, line.split()))for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            neighbours = {p for p in data if dist(point, p) <= eps}
            cluster.extend(neighbours)
            data -= neighbours
        if len(cluster) >= 30:
            center = min(cluster, key = lambda point: 
                        sum(dist(point, p) for p in cluster))
            clusters.append((cluster, center))
    return clusters
#27_18056
clustersA = clusterize1('27A_18056.txt', 1)
print(len(clustersA))

Px, Py = [], []

for _, center in clustersA:
    Px.append(center[0])
    Py.append(center[1])
Px = sum(Px) / 2
Py = sum(Py) / 2
print(abs(int(Px * 100000)), abs(int(Py * 100000)))

clustersB = clusterize1('27B_18056.txt', .3)
print(len(clustersB))

Px, Py = [], []

for _, center in clustersB:
    Px.append(center[0])
    Py.append(center[1])
Px = sum(Px) / 3
Py = sum(Py) / 3
print(abs(int(Px * 100000)), abs(int(Py * 100000)))





