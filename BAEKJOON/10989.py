# 수 정렬하기 3
# repeat:

import sys

N = int(sys.stdin.readline())

answerList = [0]*10001

for i in range(N):
    answerList[int(sys.stdin.readline())] += 1

for j in range(1, 10001):
    if answerList[j] != 0:
        for _ in range(answerList[j]):
            print(j)