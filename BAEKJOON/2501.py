# 약수 구하기
import sys

N, K = map(int, sys.stdin.readline().split())
answerList = []

for i in range(1, N+1):
    if (N % i == 0):
        answerList.append(i)
    
if (len(answerList) < K):
    print(0)
else:
    print(answerList[K-1])