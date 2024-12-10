# V
# 분해합

import sys

N = int(sys.stdin.readline())

for i in range(1, N):
    nList = list(map(int, str(i)))
    
    if (i + sum(nList)) == N:
        print(i)
        break
    
    if (i == N-1):
        print(0)
    