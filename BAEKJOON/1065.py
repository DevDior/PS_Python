# Clear
# 한수

import sys

def sol(N):
    oneNum = 0;
    if N < 100:
        oneNum = N
    else:
        oneNum = 99
        for i in range(100, N+1):
            if i//100 - (i%100)//10 == (i%100)//10 - ((i%100)%10):
                oneNum += 1

    return oneNum

N = int(sys.stdin.readline())
print(sol(N))