# 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[1] * M for i in range(N)]
r, c = 0, 0
found = False

campus = []
for i in range(N):
    row = list(input().strip())
    campus.append(row)
    # 도연이 위치 찾기
    if not found:
        if 'I' in row:
            c = i
            r = row.index('I')
            found = True

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, meet_cnt):
    stack = []
    stack.append([r, c])
    
    while stack:
        nr, nc = stack.pop()
        if campus[nc][nr] == 'P':
            meet_cnt += 1
        
        for i in range(4):
            tr, tc = nr + dr[i], nc + dc[i]
            if tr >= 0 and tr < M and tc >= 0 and tc < N and visited[tc][tr] and campus[tc][tr] != 'X':
                stack.append([tr, tc])
                visited[tc][tr] = 0
    
    if meet_cnt == 0:
        print('TT')
    else:
        print(meet_cnt)

dfs(r ,c, 0)