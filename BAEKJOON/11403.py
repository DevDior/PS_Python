# 경로 찾기
# solve: v
from collections import deque
import sys
input = sys.stdin.readline

def bfs(c):
    queue = deque()
    queue.append(c)
    
    while queue:
        now_c = queue.popleft()
        
        for i in range(N):
            if possible_path[c][i] == 0 and graph[now_c][i] == 1:
                possible_path[c][i] = 1
                queue.append(i)
        

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 각 노드별 접근 가능한 노드의 인접 행렬
possible_path = [[0] * N  for _ in range(N)]

for i in range(N):
    bfs(i)

for path in possible_path:
    print(*path)