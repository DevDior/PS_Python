import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
count_graph = [[0] * M for _ in range(N)]

'''
x, y에 대해 좌표평면(x, y)을 생각하고 문제를 풀면
이차원 리스트에서 list2[y][x]에 어색함을 느끼게 된다.
따라서 좌표평면에 대입해서 x, y를 정하는 것이 아니라
행과 열에 대입해야 하며 x, y는 단지 행과 열을 나타내는 변수라고 생각해야 한다.
그냥 r(row), c(column)으로 사용하는게 훨씬 편하다.
'''
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    count_graph[y][x] = 1
    
    while queue:
        y, x = queue.popleft()
        if y == N-1 and x == M-1:
            break
        graph[y][x] = 0
        
        for _ in range(4):
            ny = y + dy[_]
            nx = x + dx[_]
            
            if nx >= 0 and nx < M and ny >= 0 and ny < N and graph[ny][nx] == 1:
                count_graph[ny][nx] = count_graph[y][x] + 1
                queue.append([ny, nx])
                
bfs(0, 0)
print(count_graph[N-1][M-1])