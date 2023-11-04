#!/usr/bin/env python

import numpy as np
from collections import Counter

nstr = input()
cnt = Counter(nstr)
zeros = cnt['3'] + cnt['6'] + cnt['9']
ones = cnt['1'] + cnt['4'] + cnt['7']
twos = cnt['2'] + cnt['5'] + cnt['8']

mods = (ones + twos*2 + zeros*3)

if mods < 3:
    print(-1)
elif mods % 3 == 0:
    print(0)
elif mods % 3 == 1:
    if ones > 0:
        print(1)
    elif zeros > 0:
        print(ones+twos)
    else:
        print(-1)
elif mods % 3 == 2:
    if twos > 0:
        print(1)
    elif ones >= 2:
        print(2)
    elif zeros > 0:
        print(ones+twos)
    else:
        print(-1)
