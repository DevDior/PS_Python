# 유기농 배추
import sys
#from collections import deque
#sys.setrecursionlimit(10**6)
    
T = int(sys.stdin.readline())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#def DFS(target):
#    tx, ty = target[0], target[1]
#        
#    for i in range(4):
#        x = tx + dx[i]
#        y = ty + dy[i]
#        
#        if x < 0 or x >= M or y < 0 or y >= N:
#            continue
#        
#        else:
#            if [x, y] in cabbage:
#                cabbage.remove([x, y])
#                DFS([x, y])
#                
#            else:
#                continue

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage = [ list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    earthworm_count = 0
    
########## BFS ##########
    #queue = deque()
    #
    #while cabbage:
    #    earthworm_count += 1
    #    queue.append(cabbage.pop(0))
    #    
    #    while queue:
    #        target = queue.popleft()
    #        tx, ty = target[0], target[1]
    #        
    #        for i in range(4):
    #            x = tx + dx[i]
    #            y = ty + dy[i]
    #            
    #            if x < 0 or x >= M or y < 0 or y >= N:
    #                continue
    #        
    #            else:
    #                if [x, y] in cabbage:
    #                    queue.append([x, y])
    #                    cabbage.remove([x, y])
    #                    
    #                else:
    #                    continue
    #    
    #print(earthworm_count)

########## DFS - 재귀 ##########
    #while cabbage:
    #    earthworm_count += 1
    #    target = cabbage.pop(0)
    #    
    #    DFS(target)
    #                
    #print(earthworm_count)
    
    
########## DFS - Stack ##########
    stack = []
    
    while cabbage:
        earthworm_count += 1
        stack.append(cabbage.pop(0))
        
        while stack:
            target = stack.pop(-1)
            tx, ty = target[0], target[1]
            
            for i in range(4):
                x = tx + dx[i]
                y = ty + dy[i]
                
                if x < 0 or x >= M or y < 0 or y >= N:
                    continue
                else:
                    if [x, y] in cabbage:
                        stack.append([x, y])
                        cabbage.remove([x, y])
                    else:
                        continue
    
    print(earthworm_count)