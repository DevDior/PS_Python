# 단지번호붙이기
import sys
input = sys.stdin.readline

N = int(input())
house_matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

house_cnt_list =[]

def dfs(r, c):
    if not house_matrix[c][r] or visited[c][r]:
        return
    
    stack = []
    stack.append([r, c])
    house_cnt = 1
    visited[c][r] = True
    
    while stack:
        r, c = stack.pop()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N and house_matrix[nc][nr] and not visited[nc][nr]:
                stack.append([nr, nc])
                house_cnt += 1
                visited[nc][nr] = True
    
    house_cnt_list.append(house_cnt)
            
for c in range(N):
    for r in range(N):
        dfs(r, c)

house_cnt_list.sort()
print(len(house_cnt_list))
for i in range(len(house_cnt_list)):
    print(house_cnt_list[i])