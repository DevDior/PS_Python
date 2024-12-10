# Clear
# 동전0

import sys

answer = 0
N, K = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for x in range(N)]

while K != 0:
    if K >= coin_list[-1]:
        K -= coin_list[-1]
        answer += 1
    
    else:
        coin_list.pop(-1)
    
print(answer)