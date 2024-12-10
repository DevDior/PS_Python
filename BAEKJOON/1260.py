# V
# DFS와 BFS

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    matrix[s][e] = matrix[e][s] = 1

"""
# DFS(재귀)
def DFS(V):
    dfs_visited[V] = True
    print(V, end=' ')
    
    for i in range(1, N+1):
        if dfs_visited[i] == False and matrix[V][i] == True:
            DFS(i)
"""

# DFS(stack)
def DFS(V):
    stack = [V]
    
    while stack:
        v = stack.pop(-1)
        if dfs_visited[v] != True: print(v, end=' ')
        dfs_visited[v] = True
        
        for i in range(N, 0, -1):
            if dfs_visited[i] == False and matrix[v][i] == True:
                stack.append(i)
    
def BFS(V):
    queue = deque()
    queue.append(V)
    bfs_visited[V] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in range(1, N+1):
            if bfs_visited[i] == False and matrix[v][i] == True:
                bfs_visited[i] = True
                queue.append(i)


DFS(V)
print()
BFS(V)