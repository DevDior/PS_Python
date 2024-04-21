import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(y, x):
    if y >= N or y < 0 or x >= M or x < 0:
        return False
    
    if graph[y][x] == 1:
        return False
    else:
        graph[y][x] = 1
        for _ in range(4):
            ny = y + dy[_]
            nx = x + dx[_]
            dfs(ny, nx)
        return True

answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            answer += 1

print(answer)
