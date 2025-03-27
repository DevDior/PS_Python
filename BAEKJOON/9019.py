# Clear
# DSLR

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False]*10000
    q = deque([(A, '')])
    
    while q:
        num, cmd = q.popleft()
        if num == B:
            print(cmd)
            break
        if not visited[num]:
            visited[num] = True
            q.append((num*2%10000, cmd+'D'))
            q.append((num-1 if num != 0 else 9999, cmd+'S'))
            q.append((num%1000*10+num//1000, cmd+'L'))
            q.append((num%10*1000+num//10, cmd+'R'))
        else:
            continue