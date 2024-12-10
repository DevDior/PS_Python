# Clear
# 좌표 정렬하기

import sys

N = int(sys.stdin.readline())
answerList = []

for i in range(N):
    answerList.append(list(map(int, sys.stdin.readline().split())))

answerList.sort()

for j in answerList:
    print(j[0], end=' ')
    print(j[1])