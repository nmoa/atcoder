#!/usr/bin/env python

import numpy as np

n = map(int, input().split())
aa = list(map(int, input().split()))
aa = np.array(aa)
gcd = []

for i in range(2, max(aa)+1):
    gcd.append(np.count_nonzero(aa % i == 0))

print(gcd.index(max(gcd))+2)
