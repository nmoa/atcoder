#!/usr/bin/env python

import numpy as np

n = int(input())

l = []
for i in range(int(np.sqrt(n))):
    j = i+1
    if n/j == int(n/j):
        l.append(j)
        if j != n/j:
            l.append(n/j)

arr = np.array(l)
list_sorted = np.sort(arr).tolist()
for i in list_sorted:
    print(int(i))