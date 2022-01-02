# 요세푸스 문제0

import sys

N, K = map(int, sys.stdin.readline().split())
numList = list(x for x in range(1, N+1))

C = K-1
print('<', end='')
for _ in range(N):
    if C >= len(numList):
        C = C % len(numList)
        
    if len(numList) != 1:
        print(numList.pop(C), end='')
        print(',', end=' ')
    else:
        print(numList.pop(C), end='')
        
    C += K-1
        
print('>')