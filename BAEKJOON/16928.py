# Clear
# 뱀과 사다리 게임

import sys
from collections import deque
intput = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * 10 for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]
ladder = {}
snake = {}

for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end

def bfs():
    # (c, r)
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True
    
    while queue:
        c, r = queue.popleft()
        int_location = c * 10 + r
        
        for i in range(1, 7):
            n_int_location = int_location + i
            if n_int_location > 99:
                break
            
            nc = n_int_location // 10
            nr = n_int_location % 10
            n_count = board[c][r] + 1
            
            if visited[nc][nr] == True:
                continue
            else:
                board[nc][nr] = n_count
                visited[nc][nr] = True
                
                # 사다리 만날 때
                if n_int_location + 1 in ladder:
                    n_int_location = ladder.get(n_int_location + 1) - 1
                    nc = n_int_location // 10
                    nr = n_int_location % 10
                    
                    if visited[nc][nr] == False:
                        board[nc][nr] = n_count
                        visited[nc][nr] = True
                        queue.append([nc, nr])
                    
                # 뱀 만날 때
                elif n_int_location + 1 in snake:
                    n_int_location = snake.get(n_int_location + 1) - 1
                    nc = n_int_location // 10
                    nr = n_int_location % 10
                    
                    if visited[nc][nr] == False:
                        board[nc][nr] = n_count
                        visited[nc][nr] = True
                        queue.append([nc, nr])
                
                else:
                    queue.append([nc, nr])
        
bfs()

print(board[-1][-1])