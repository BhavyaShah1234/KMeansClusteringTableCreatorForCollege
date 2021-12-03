import pandas as pd
import random as rn


def distance(row, point):
    dist = 0
    for p in range(len(point)):
        dist = pow(row[p] - point[p], 2) + dist
    dist = pow(dist, 0.5)
    return dist


def minimum(row):
    m = 10000000000000000
    ind = k + 1
    for p in range(k):
        if row[p] < m:
            m = row[p]
            ind = p
    return ind + 1


# SETTINGS TO CHANGE NATURE OF INITIAL POINTS
iterations = 3
random_init = False
k = 3

if random_init:
    init_points = []
    for i in range(k):
        init_points.append([rn.randint(0, 100),
                            rn.randint(0, 100)])
else:
    # IF INITIAL CENTROIDS ARE GIVEN THEN FILL THEM HERE
    init_points = [[190, 73],
                   [185, 76],
                   [180, 70]]

# FILL THE GIVEN DATASET AS FOLLOWS
df = pd.DataFrame({'X': [190, 175, 165, 172, 185, 154, 171, 180, 183, 165],
                   'Y': [73, 59, 70, 65, 76, 75, 81, 70, 84, 82]})
print(df)
print(init_points)

for q in range(iterations):
    d = pd.DataFrame()
    # CALCULATING DISTANCES FROM EACH CENTROID
    for i in range(k):
        d[f'C{i+1}'] = df.apply(lambda x: distance(x, init_points[i]), axis=1)

    dist_cols = [f'C{i+1}' for i in range(k)]
    # GET MINIMUM DISTANCE CLUSTER AND ASSIGN IT
    d['Cluster'] = d[dist_cols].apply(lambda x: minimum(x), axis=1)
    print(d)

    # SHIFT CENTROIDS
    for i in range(k):
        temp = df[d['Cluster'] == i + 1]
        for j in range(temp.shape[1]):
            add = temp.iloc[:, j].sum()
            add = add / temp.shape[0]
            init_points[i][j] = add
    print(init_points)
