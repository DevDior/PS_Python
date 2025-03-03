# Clear
# 배

import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort()
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort()
moved_boxes = [0 for _ in range(m)]

if cranes[-1] < boxes[-1]:
    print(-1)
    
else:
    take_min = 0
    
    while 0 in moved_boxes:
        for i in range(n-1, -1, -1):
            if cranes[i] < boxes[0]:
                continue
            
            for j in range(m-1, -1, -1):
                if moved_boxes[j] != 1 and boxes[j] <= cranes[i]:
                    moved_boxes[j] = 1
                    break
        
        take_min += 1
    
    print(take_min)