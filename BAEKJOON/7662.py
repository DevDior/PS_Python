# V
# 이중 우선순위 큐

import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    deleted = [False]*1000001
    
    for i in range(k):
        command, num = input().split()
        num = int(num)
        
        if command == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
        else:
            if num == 1:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
            else:
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
    
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')