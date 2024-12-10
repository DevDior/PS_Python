# Clear
# 계단 오르기

import sys

#DP
N = int(sys.stdin.readline())
score_list = [int(sys.stdin.readline()) for x in range(N)]

if N >= 2:
    d = [[0, 0] for x in range(N)]    # index 0 = 점프 해야할 때, index 1 = 점프 안해도 될 때
    d[0][1] = score_list[0]
    d[1] = [sum(score_list[:2]), score_list[1]]
    
    for i in range(2, N):
        d[i][0] = d[i-1][1] + score_list[i]
        d[i][1] = max(d[i-2]) + score_list[i]

    print(max(d[N-1]))
    
else:
    print(score_list[0])