# 소수 구하기

import sys

M, N = map(int, sys.stdin.readline().split())
answer = []

for i in range(M, N+1):
    isMinority = True
    
    if i == 1:
        isMinority = False
    elif i == 2:
        isMinority = True
    elif i % 2 == 0:
        isMinority = False
    else:
        for j in range(3, i//2 + 1, 2):
            if i % j == 0:
                isMinority = False
                break
    
    if isMinority == True:
        answer.append(i)
        
for k in answer:
    print(k)