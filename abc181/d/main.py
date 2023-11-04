#!/usr/bin/env python

import numpy as np


def countup(l):
    result = []
    result.append(l.count('1'))
    result.append(l.count('2'))
    result.append(l.count('3'))
    result.append(l.count('4'))
    result.append(l.count('5'))
    result.append(l.count('6'))
    result.append(l.count('7'))
    result.append(l.count('8'))
    result.append(l.count('9'))
    return result


instr = input()
innum = int(instr)
s = list(instr)

if innum < 10:
    if innum % 8 == 0:
        print('Yes')
    else:
        print('No')
elif innum < 100:
    if innum % 8 == 0:
        print('Yes')
    else:
        swapped = int(s[1] + s[0])
        if swapped % 8 == 0:
            print('Yes')
        else:
            print('No')
else:
    s2 = countup(s)
    eights = []

    for i in range(13, 125):
        eights_str = list(str(i*8))
        if eights_str.count('0') > 0:
            continue
        else:
            eights.append(countup(eights_str))

    is_found = False

    for eight in eights:
        is_found = (s2[0] >= eight[0]) and (s2[1] >= eight[1]) and (s2[2] >= eight[2]) and (s2[3] >= eight[3]) and (
            s2[4] >= eight[4]) and (s2[5] >= eight[5]) and (s2[6] >= eight[6]) and (s2[7] >= eight[7]) and (s2[8] >= eight[8])
        if is_found:
            break

    if is_found:
        print('Yes')
    else:
        print('No')
