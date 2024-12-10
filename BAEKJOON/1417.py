# Clear
# 국회의원 선거

import sys
import heapq

input = sys.stdin.readline

N = int(input())
dasom = 0
answer = 0
heap = []

for _ in range(N):
    x = int(input())
    heapq.heappush(heap, (-x, x))
    if _ == 0:
        dasom = x


if len(heap) == 1:
    print(answer)
else:
    while True:
        max_votes = heapq.heappop(heap)[1]
        if max_votes == dasom and heap[0][1] != dasom:
            break
        else:
            heapq.heappush(heap, (-(max_votes-1), max_votes-1))
            
            dasom += 1
            heapq.heappush(heap, (-dasom, dasom))
            answer += 1
        
    print(answer)