#!/usr/bin/env python

n = int(input())

result = 0

for i in range(n):
    l = input().split(' ')
    a = int(l[0])
    b = int(l[1])
    result += (b - a + 1) * (a + b) / 2

print(int(result))
