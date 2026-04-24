""" from math import *

def find_Px_Py(clusters):
    centersX = []
    centersY = []
    for cluster in clusters:
        center = min(cluster, key = lambda point: sum(dist(point, p1) for p1 in cluster))
        centersX.append(center[0])
        centersY.append(center[1])
    Px = sum(centersX) / len(centersX)
    Py = sum(centersY) / len(centersY)
    return abs(int(Px * 10000)), abs(int(Py * 10000))


clustersA = [[], [], []]

data = {tuple(map(float, line.split())) for line in open('27_A_21599 (1).txt')}

for point in data:
    x, y = point
    if y >= x - 10:
        clustersA[0].append(point)
    if y < x - 10 and y >= -5:
        clustersA[1].append(point)
    if y < -5:
        clustersA[2].append(point)

print(find_Px_Py(clustersA))


clustersB = [[], [], [], [], [], []]

data = {tuple(map(float, line.split())) for line in open('27_B_21599 (1).txt')}

for point in data:
    x, y = point
    if y <= -8/3 * x - 104 / 3:
        clustersB[0].append(point)
    elif x <= -10:
        clustersB[1].append(point)
    elif y >= 2 * x + 14:
        clustersB[2].append(point)
    elif y >= x + 1:
        clustersB[3].append(point)
    elif y >= -5:
        clustersB[4].append(point)
    else:
        clustersB[5].append(point)

print(find_Px_Py(clustersB))


def clusterize(file, eps):
    data = {tuple(map(float, line.split())) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            n = {p1 for p1 in data if dist(point, p1) <= eps}
            cluster.extend(n)
            data -= n
        if len(cluster) >= 30:
            center = min(cluster, key = lambda point: sum(dist(point, p1) for p1 in cluster))
            clusters.append((cluster, center))
    return clusters

clustersA = clusterize('27A_18678 (3).txt', .5)
Px = sum(center[0] for _, center in clustersA) / 2
Py = sum(center[1] for _, center in clustersA) / 2
print(int(Px * 100000), int(Py * 100000))


clustersA = clusterize('27B_18678 (3).txt', .5)
Px = sum(center[0] for _, center in clustersA) / 3
Py = sum(center[1] for _, center in clustersA) / 3
print(int(Px * 100000), int(Py * 100000)) """

#29079

from math import dist

def centerize(cluster):
    return min(cluster, key = lambda point: sum(dist(point[0], p1[0]) for p1 in cluster))

clustersA = [[], []]

data = {(tuple(map(float, line.split()[:2])), line.split()[2]) for line in open('27_A_29079.txt')}

for point in data:
    x, y = point[0]
    if y <= 8:
        clustersA[0].append(point)
    else:
        clustersA[1].append(point)

centers = []
for cluster in clustersA:
    centers.append(centerize(cluster))

orange_subg_1 = [point[0] for point in clustersA[0] if point[1][0] == 'N' and 'IV' in point[1]]
orange_subg_2 = [point[0] for point in clustersA[1] if point[1][0] == 'N' and 'IV' in point[1]]

A1 = min(
    dist(min(orange_subg_2, key = lambda point: dist(centers[0][0], point)), centers[0][0]),
    dist(min(orange_subg_1, key = lambda point: dist(centers[1][0], point)), centers[1][0])
)

A2 = max(
    dist(max(orange_subg_2, key = lambda point: dist(centers[0][0], point)), centers[0][0]),
    dist(max(orange_subg_1, key = lambda point: dist(centers[1][0], point)), centers[1][0])
)

print(int(A1 * 10000), int(A2 * 10000))

clustersB = [[], [], []]

data = {(tuple(map(float, line.split()[:2])), line.split()[2]) for line in open('27_B_29079.txt')}

for point in data:
    x, y = point[0]
    if y >= 22:
        clustersB[0].append(point)
    elif x <= 22:
        clustersB[1].append(point)
    else:
        clustersB[2].append(point)
print(len(clustersB))

max_clustersB = max(clustersB, key = lambda cluster: len(cluster))
min_clustersB = min(clustersB, key = lambda cluster: len(cluster))

B1, B2 = float('-inf'), float('-inf')
for point in max_clustersB:
    if point[1][0] == 'J' and point[1][2:] == 'V':
        B1 = max(B1, point[0][0])

for point in min_clustersB:
    if point[1][0] == 'J' and point[1][2:] == 'V':
        B2 = max(B2, point[0][1])
print(int(B1 * 10000), int(B2 * 10000))

#29078

def clusterize(file, eps):
    data = {(tuple(map(float, line.split()[:2])), line.split()[2]) for line in open(file)}
    clusters = []
    while data:
        cluster = [data.pop()]
        for point in cluster:
            n = {p1 for p1 in data if dist(p1[0], point[0]) <= eps}
            cluster.extend(n)
            data -= n
        center = min(cluster, key = lambda point: sum(dist(point[0], p1[0]) for p1 in cluster))
        clusters.append((cluster, center))
    return clusters

clustersA = clusterize('27_A_29078.txt', 1)
max_clustersA_G5 = max(clustersA, key = lambda cluster: 
                       sum(1 for point in cluster[0] if point[1][:2] == 'G5'))
A1 = max_clustersA_G5[1][0][0]
print(int(A1 * 10000))
min_clustersA_G5 = min(clustersA, key = lambda cluster: 
                       sum(1 for point in cluster[0] if point[1][:2] == 'G5'))
A2 = min_clustersA_G5[1][0][1]
print(int(A2 * 10000))

clustersB = clusterize('27_B_29078.txt', 1)
clustersB.sort(key = lambda cluster: len(cluster[0]))

dists_B1 = [dist(point[0], clustersB[-1][1][0]) for point in clustersB[-1][0] if point[1][2:] == 'II']
B1 = sum(dists_B1) / len(dists_B1)
print(int(B1 * 10000))

dists_B2 = [dist(point[0], clustersB[0][1][0]) for point in clustersB[0][0] if point[1][2:] == 'II']
B2 = sum(dists_B2) / len(dists_B2)
print(int(B2 * 10000))