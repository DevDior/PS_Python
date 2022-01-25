# 랜선 자르기 v

import sys

K, N = map(int, sys.stdin.readline().split())
lanList = []

for _ in range(K):
    lanList.append(int(sys.stdin.readline()))
#    
#maxLan = max(lanList)
#answer = 0
#
#for i in range(maxLan, 0, -1):
#    count = 0
#    
#    for j in lanList:
#        count += j//i
#    
#    if count >= N: 
#        answer = i
#        break
#        
#print(answer)

start = 1
end = max(lanList)

while start <= end:
    count = 0
    mid = (start + end)//2
    
    for i in lanList:
        count += i//mid
    
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)