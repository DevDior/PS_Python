# Clear
# 쉬운 최단거리

import sys
from collections import deque
input = sys.stdin.readline

n ,m = map(int, input().split())
graph = []
count_graph = [[-1] * m for _ in range(n)]
dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]
tc = None
tr = None

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            tc = i
            tr = j
        elif graph[i][j] == 0:
            count_graph[i][j] = 0

def bfs(c, r):
    queue = deque([[c, r]])
    count_graph[c][r] = 0
    
    while queue:
        c, r = queue.popleft()
        
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if nc >= 0 and nc < n and nr >=0 and nr < m and count_graph[nc][nr] == -1:
                if graph[nc][nr] != 0:
                    queue.append([nc, nr])
                    count_graph[nc][nr] = count_graph[c][r] + 1

bfs(tc, tr)

for count_list in count_graph:
    for i, count in enumerate(count_list):
        if i != m - 1:
            print(count, end=' ')
        else:
            print(count)