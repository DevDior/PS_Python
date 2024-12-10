# Clear
# 구간 합 구하기 4

import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = []
sum_list.append(num_list[0])

for i in range(1, N):
    sum_list.append(sum_list[i-1] + num_list[i])

for _ in range(M):
    i, n = map(int, sys.stdin.readline().split())
    if i == n:
        print(num_list[i-1])
    elif i == 1:
        print(sum_list[n-1])
    else:
        print(sum_list[n-1] - sum_list[i-2])