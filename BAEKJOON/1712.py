# Clear
# 손익분기점

from sys import stdin

A, B, C = map(int, stdin.readline().split())
n = 0

if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)