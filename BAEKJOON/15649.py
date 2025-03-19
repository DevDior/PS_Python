# V
# N과 M(1)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def dfs():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
    else:
        for i in range(1, N+1):
            if i not in answer:
                answer.append(i)
                dfs()
                answer.pop()

dfs()