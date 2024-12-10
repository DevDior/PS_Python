# Clear
# 미로 탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

queue.append([0, 0])
bfs()
print(matrix[N-1][M-1])