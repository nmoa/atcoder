#!/usr/bin/env python

import itertools
import numpy as np

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

n = int(input())

points = []

for i in range(n):
    l = input().split(' ')
    l = [int(a) for a in l]
    points.append(l)

points = get_unique_list(points)

n_points = len(points)

flag = False

for i,j,k in itertools.product(points, points, points):
    if (i == j) or (i == k) or (j == k):
        continue
    dx1 = i[0] - j[0]
    dy1 = i[1] - j[1]
    dx2 = i[0] - k[0]
    dy2 = i[1] - k[1]
    if (dx1*dy2 - dx2*dy1 == 0):
        # print(i, j, k)
        print('Yes')
        flag = True
        break

if not(flag):
    print('No')
