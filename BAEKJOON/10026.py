#
# 적록색약

import sys
input = sys.stdin.readline

N = int(input())
picture = []
normal_visited = [False * N] * N
red_green_medicine_visited = [False * N] * N
stack = []

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

normal_user_cnt = 0
red_green_medicine_cnt = 0

for _ in range(N):
    picture.append(list(input().split()))

def dfs(c, r, color, kind):
    if kind == 'normal':
        normal_visited[c][r] = True
    else:
        red_green_medicine_visited[c][r] = True
        
    
for c in range(N):
    for r in range(N):
        if not normal_visited[c][r]:
            stack.append((c, r, picture[c][r]))
            dfs(c, r, picture[c][r], 'normal')
            normal_user_cnt += 1
        
        if not red_green_medicine_visited[c][r]:
            stack.append((c, r, picture[c][r]))
            dfs(c, r, picture[c][r], 'red-green')
            red_green_medicine_cnt += 1

print(f"{normal_user_cnt} {red_green_medicine_cnt}")