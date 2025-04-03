#
# 테트로미노

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
visited = [[False] * M for _ in range(N)]
max_value = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]