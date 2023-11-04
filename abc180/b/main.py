#!/usr/bin/env python

import numpy as np

n = int(input())
l = input().split(' ')
l = [int(n) for n in l]

arr = np.abs(np.array(l))

print(arr.sum())
print(np.sqrt(np.sum(arr**2)))
print(arr.max())