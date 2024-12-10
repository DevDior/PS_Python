# Clear
# 색종이 만들기

import sys

N = int(sys.stdin.readline())
colored_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white_count = 0
blue_count = 0

def solution(x, y, n):
    global colored_paper, white_count, blue_count
    
    for i in range(y, y+n):
        for j in range(x, x+n):
            if colored_paper[y][x] != colored_paper[i][j]:
                for k in range(2):
                    for l in range(2):
                        solution(x+k*n//2, y+l*n//2, n//2)
                return
    
    if colored_paper[y][x] == 0:
        white_count += 1
    elif colored_paper[y][x] == 1:
        blue_count += 1

solution(0, 0, N)
print(white_count)
print(blue_count)