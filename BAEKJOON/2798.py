# Clear
# 블랙잭

import sys

N, M = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in cardList:
    for j in cardList[cardList.index(i)+1:]:
        for k in cardList[cardList.index(j)+1:]:
            if i+j+k > answer and i+j+k <= M:
                answer = i+j+k

print(answer)