# V
# 최소 힙

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(heapq.heappop(heap))
        
        except IndexError:
            print(0)
    else:
        heapq.heappush(heap, x)