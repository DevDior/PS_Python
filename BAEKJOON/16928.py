#
# 뱀과 사다리 게임

import sys
from collections import deque
intput = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * 10 for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]
ladder = {}
snake = {}
answer = 0

for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end

def bfs():
    # (c, r)
    queue = deque((0, 0))
    visited[0][0] = True
    
    while queue:
        c, r, count = queue.popleft()
        
        if r < 9:
            nr = r + 1
            nc = c
        elif c < 9:
            nr = 0
            nc = c + 1
        else:
            continue
        n_count = board[c][r] + 1
        
        # 사다리 만날 때
        ladder_c = nc
        ladder_r = nr
        while ladder.get(ladder_c * 10 + ladder_r):
            ladder_value = ladder.get(ladder_c * 10 + ladder_r)
            board[ladder_c][ladder_r] = n_count
            visited[ladder_c][ladder_r] = True
            
            ladder_c
            
        else:
            queue.append((ladder_c, ladder_r))
        
        # 뱀 만날 때
        
        # 안만날 때
        
bfs()

print(board[-1][-1])