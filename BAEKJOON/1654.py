# 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())
lanList = []

for _ in range(K):
    lanList.append(int(sys.stdin.readline()))
    
maxLan = max(lanList)
answer = 0

for i in range(maxLan, 0, -1):
    count = 0
    
    for j in lanList:
        count += j//i
    
    if count >= N:
        answer = i
        break
        
print(answer)