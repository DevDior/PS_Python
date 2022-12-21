# 1로 만들기
import sys

N = int(sys.stdin.readline())

# DP Bottom-UP
memo = [0 for x in range(N+1)]     # d[i] = i에서 1로 가는 최소 연산

for i in range(2, N+1):
    memo[i] = memo[i-1] + 1           # d[i-1]의 최소 연산 + '-1'의 연산
    
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i//3]+1)     # d[i//3]의 최소 연산 + '/3'의 연산
    
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i//2]+1)     # d[i//2]의 최소 연산 + '/2'의 연산    


print(memo[N])



# DP Top-Down


# DP BFS