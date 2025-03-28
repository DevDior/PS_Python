#
# 적록색약

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
picture = []
normal_visited = [[False] * N for _ in range(N)]
red_green_medicine_visited = [[False] * N for _ in range(N)]

dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]

normal_user_cnt = 0
red_green_medicine_cnt = 0

for _ in range(N):
    picture.append(list(input().rstrip()))

def dfs(c, r, check_color, kind):
    if kind == 'normal' and picture[c][r] != check_color:
        return
    else:
        if check_color in ['R', 'G']:
            if picture[c][r] == 'B':
                return
        else:
            if picture[c][r] != check_color:
                return
    
    if kind == 'normal':
        normal_visited[c][r] = True
    else:
        red_green_medicine_visited[c][r] = True
    
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        
        if nc >= 0 and nc < N and nr >= 0 and nr < N:
            if kind == 'normal' and normal_visited[nc][nr] == False:
                dfs(nc, nr, check_color, 'normal')
            elif kind == 'red-green' and red_green_medicine_visited[nc][nr] == False:
                dfs(nc, nr, check_color, 'red-green')
        
    
for c in range(N):
    for r in range(N):
        if not normal_visited[c][r]:
            dfs(c, r, picture[c][r], 'normal')
            normal_user_cnt += 1
        
        if not red_green_medicine_visited[c][r]:
            dfs(c, r, picture[c][r], 'red-green')
            red_green_medicine_cnt += 1

print(f"{normal_user_cnt} {red_green_medicine_cnt}")