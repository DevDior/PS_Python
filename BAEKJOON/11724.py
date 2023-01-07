# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
answer = 0

matrix = [[0] * (N+1) for i in range(N+1)]
visited = [0] * (N+1)


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u][v] = matrix[v][u] = 1

def DFS(n):
    visited[n] = 1
    
    for i in range(1, N+1):
        if visited[i] == 0 and matrix[n][i] == 1:
            DFS(i)

while True:
    if 0 in visited[1:]:
        DFS(visited[1:].index(0)+1)
        answer += 1
    else:
        break

print(answer)