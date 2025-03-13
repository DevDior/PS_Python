# V
# 토마토

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

queue = deque()
answer = 0
all_tomatoes_ripen = True

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                queue.append([x, y, z])
            elif graph[z][y][x] == 0:
                all_tomatoes_ripen = False

def bfs():
    while queue:
        x, y, z = queue.popleft()
    
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append([nx, ny, nz])

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                sys.exit()
        answer = max(answer, max(j))

if answer == 1:
    # 모든 토마토가 익은 상태
    print(0)
else:
    print(answer - 1)