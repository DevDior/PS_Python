# Clear
# Z

import sys

N, r, c = map(int, sys.stdin.readline().split())
answer = 0

def solution(x, y, n):
    global answer
    
    if n == 0:
        return

    split_size = (2**n//2)**2
    
    # 1사분면
    if x >= 2**n//2 and y < 2**n//2:
        answer += split_size
        solution(x-2**n//2, y, n-1)
    # 2사분면
    elif x < 2**n//2 and y < 2**n//2:
        solution(x, y, n-1)
    # 3사분면
    elif x < 2 **n//2 and y >= 2**n//2:
        answer += split_size * 2
        solution(x, y-2**n//2, n-1)
    # 4사분면
    else:
        answer += split_size * 3
        solution(x-2**n//2, y-2**n//2, n-1)
    
    return answer

print(solution(c, r, N))