# Clear
# 프린터 큐

import sys

T = int(sys.stdin.readline())

for i in range(T):
    answer = 0
    n, w = map(int, sys.stdin.readline().split())
    q = list(map(int, sys.stdin.readline().split()))
    while(1):
        if max(q) == q[0]:
            if w == 0:
                answer += 1
                break
            q.pop(0)
            if w > 0: w -= 1
            answer += 1
        else:
            q.append(q.pop(0))
            w -= 1
            if w < 0: w = len(q) - 1
    print(answer)