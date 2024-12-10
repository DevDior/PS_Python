# V
# 덩치

import sys

N = int(sys.stdin.readline())
group = []

for _ in range(N):
    group.append(tuple(map(int, sys.stdin.readline().split())))
    
for i in range(N):
    rank = 1
    
    for j in range(N):
        if group[i][0] < group[j][0] and group[i][1] < group[j][1]:
            rank += 1
    print(rank, end=' ')