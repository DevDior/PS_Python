# V
# 통계학

import sys
import collections

N = int(sys.stdin.readline())
numList = []

for _ in range(N):
    numList.append(int(sys.stdin.readline()))
numList.sort()

count = collections.Counter(numList)
maxDuplicateNumList = count.most_common()
maxDuplicateNumList.sort(reverse=True, key=lambda x : x[1])

if len(maxDuplicateNumList) == 1:
    maxDuplicateNum = maxDuplicateNumList[0][0]
else:
    if maxDuplicateNumList[0][1] == maxDuplicateNumList[1][1]:
        maxDuplicateNum = maxDuplicateNumList[1][0]
    else:
        maxDuplicateNum = maxDuplicateNumList[0][0]
          
sumNum = sum(numList)
if ((sumNum/N)*10) % 10 >= 5:
    print(sumNum//N+1)
else:
    print(sumNum//N)
    
print(numList[N//2])
print(maxDuplicateNum)

if N == 1:
    print(0)
else:
    print(max(numList)-min(numList))