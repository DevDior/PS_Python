# Clear
# OX퀴즈

import sys

T = int(sys.stdin.readline())

for i in range(T):
    sol = sys.stdin.readline()
    score = 0
    total_score = 0

    for j in sol:
        if j == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    
    print(total_score)