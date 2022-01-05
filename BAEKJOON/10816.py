# 숫자 카드2

import sys

N = int(sys.stdin.readline())
NList = list(map(int, sys.stdin.readline().split()))
NList.sort()
M = int(sys.stdin.readline())
MList = list(map(int, sys.stdin.readline().split()))

answerDic = {x:0 for x in MList}

for i in NList:
    if i in answerDic:
        answerDic[i] += 1
        
for j in MList:
    print(answerDic[j], end=' ')