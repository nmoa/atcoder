#!/usr/bin/env python

n = map(int, input().split())
aa = list(map(int, input().split()))

moves = []
pos = 0
maxpos = 0
for a in aa:
    pos += a
    maxpos = pos if pos > maxpos else maxpos
    moves.append(tuple((pos, maxpos)))

pos = 0
maxpos2 = 0
for move in moves:
    maxpos2 = pos + move[1] if pos + move[1] > maxpos2 else maxpos2
    pos += move[0]
print(maxpos2)
