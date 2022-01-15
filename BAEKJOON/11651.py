# 좌표 정렬하기 2

import sys

N = int(sys.stdin.readline())

numList = []

for _ in range(N):
    numList.append(list(map(int ,sys.stdin.readline().split())))
    
numList.sort(key=lambda x :(x[1], x[0]))

for i in numList:
    print(i[0], end=' ')
    print(i[1])