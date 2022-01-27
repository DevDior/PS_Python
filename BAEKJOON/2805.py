# 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().split())
treeList = list(map(int, sys.stdin.readline().split()))
end = max(treeList)
start = 0

while start <= end:
    carryTree = 0
    mid = (start + end)//2
    
    for i in treeList:
        if i > mid:
            carryTree += i - mid
    
    if carryTree >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)