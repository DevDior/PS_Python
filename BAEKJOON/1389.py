# V
# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

def bfs(graph, start):
    global count_result
    
    count = [0 for _ in range(len(graph))]
    visited = [start]
    queue = deque()
    queue.append(start)
    
    while queue:
        target = queue.popleft()
        for i in graph[target]:
            if not i in visited:
                count[i] = count[target] + 1
                visited.append(i)
                queue.append(i)    
        
    return sum(count)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
count_result = [0 for _ in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, N+1):
    count_result[j-1] = bfs(graph, j)

print(count_result.index(min(count_result))+1)