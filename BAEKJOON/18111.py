# 마인크래프트
import sys

N, M ,B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for n in range(N)]
answer_height = 0
answer_time = sys.maxsize

for _ in range(257):
    add_block = 0
    minus_block = 0
    
    for i in range(N):
        for j in range(M):
            if ground[i][j] > _:
                add_block += ground[i][j] - _
                
            else:
                minus_block += _ - ground[i][j]
    
    if B + add_block >= minus_block:
        if add_block * 2 + minus_block <= answer_time:
            answer_time = add_block * 2 + minus_block
            answer_height = _
        
print(answer_time, answer_height)