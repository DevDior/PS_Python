# 종이의 개수
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
minus_one_count = 0
zero_count = 0
one_count = 0

def solution(x, y, n):
    global paper, minus_one_count, zero_count, one_count
    start_paper = paper[x][y]
    
    # 분할정복
    for i in range(x, x+n):
        for j in range(y, y+n):
            if start_paper != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        solution(x+k*n//3, y+l*n//3, n//3)
                return
            
    if start_paper == -1:
        minus_one_count += 1
    elif start_paper == 0:
        zero_count += 1
    elif start_paper == 1:
        one_count += 1

solution(0, 0, N)
print(minus_one_count)
print(zero_count)
print(one_count)