# V
# 테트로미노

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

# 방향: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * M for _ in range(N)]

# DFS로 4칸짜리 테트로미노 만들기
def dfs(r, c, count, total):
    global max_value
    if count == 4:
        max_value = max(max_value, total)
        return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, count + 1, total + board[nr][nc])
            visited[nr][nc] = False

# DFS로 만들 수 없는 ㅗ, ㅜ, ㅓ, ㅏ 모양 처리
def check_exception_shapes(r, c):
    global max_value
    for shape in [
        [(0, 0), (-1, 0), (0, 1), (0, -1)],  # ㅗ
        [(0, 0), (1, 0), (0, 1), (0, -1)],   # ㅜ
        [(0, 0), (0, -1), (1, 0), (-1, 0)],  # ㅓ
        [(0, 0), (0, 1), (1, 0), (-1, 0)]    # ㅏ
    ]:
        total = 0
        is_valid = True
        for dr_offset, dc_offset in shape:
            nr = r + dr_offset
            nc = c + dc_offset
            if 0 <= nr < N and 0 <= nc < M:
                total += board[nr][nc]
            else:
                is_valid = False
                break
        if is_valid:
            max_value = max(max_value, total)

# 모든 위치에서 DFS와 예외 모양 체크
for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False
        check_exception_shapes(r, c)

print(max_value)
