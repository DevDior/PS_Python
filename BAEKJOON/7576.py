# V
# 토마토

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
answer = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit()
    answer = max(answer, max(i))
print(answer-1)
