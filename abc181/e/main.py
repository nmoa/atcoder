#!/usr/bin/env python

import numpy as np

n, m = map(int, input().split())
hs = list(map(int, input().split()))
hs.sort()
ws = list(map(int, input().split()))
ws.sort()

h0 = hs[0::2] - hs[1::2]
h1 = hs[1::2] - hs[2::2]
i = 0
# for w in ws:
