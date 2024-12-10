# V
# 숨바꼭질

from dis import dis
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
distance_time = [0] * (10**5 + 1)

def BFS(n, k):
    queue = deque()
    queue.append(N)
    
    while queue:
        target = queue.popleft()
        if target == k:
            return distance_time[target]
        
        if target == 0:
            valiable_target = [target+1, target*2]
        elif target <= 50000:
            valiable_target = [target-1, target+1, target*2]
        elif target == 100000:
            valiable_target = [target-1]
        else:
            valiable_target = [target-1, target+1]
        
        for i in valiable_target:
            if not distance_time[i]:
                distance_time[i] = distance_time[target] + 1
                queue.append(i)
                
print(BFS(N, K))