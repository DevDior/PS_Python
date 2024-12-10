# V
# ATM

import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
answer = 0
add_value = 0

# # 버블 정렬 O(n^2), 케이스 최악 100만 회, 파이썬 1초에 2000만 회
# c = len(P) - 1
# 
# while c:
#     for i in range(c):
#         if P[i] > P[i+1]: P[i], P[i+1] = P[i+1], P[i]
#         
#     c -= 1

# 퀵정렬로 풀기

# 병합정렬로 풀기

for j in P:
    add_value = add_value + j
    answer += add_value
    
print(answer)