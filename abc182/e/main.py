#!/usr/bin/env python

import numpy as np

h, w, n, m = map(int, input().split())
lights = []
blocks = []
for i in range(n):
    x, y = map(int, input().split())
    lights.append(tuple((x-1, y-1)))
for i in range(m):
    x, y = map(int, input().split())
    blocks.append(tuple((x-1, y-1)))
field = np.zeros((h, w))
for b in blocks:
    field[b[0], b[1]] = 2
for l in lights:
    field[l[0], l[1]] = 1
for i in range(h):
    if np.any(field[i] == 1):
        l = np.where(field[i] == 1)[0]
        b = np.where(field[i] == 2)[0]

    # # 横方向
    # if np.any(field[l[0]] == 2):
    #     bind = np.where(field[l[0]] == 2)[0]
    #     left = max(bind[bind < l[1]]) if (bind < l[1]).any() else 0
    #     right = min(bind[bind > l[1]]) if (bind > l[1]).any() else w
    #     field[l[0], left+1:right] = 1
    # else:
    #     field[l[0]] = 1
    # # 縦方向
    # if np.any(field[:, l[1]] == 2):
    #     bind = np.where(field[:, l[1]] == 2)[0]
    #     left = max(bind[bind < l[0]]) if (bind < l[0]).any() else 0
    #     right = min(bind[bind > l[0]]) if (bind > l[0]).any() else h
    #     field[left+1:right, l[1]] = 1
    # else:
    #     field[:, l[1]] = 1
print(np.count_nonzero(field == 1))
