# 마인크래프트

import sys

def remove_block(n):
    return n*2
    
def put_block(n):
    return n

N, M ,B = map(int, sys.stdin.readline().split())
fieldMap = []
answer = [sys.maxsize, 0]
total_block = 0
avg = 0

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    fieldMap.append(line)
    total_block += sum(line)

avg = (total_block+B)//(N*M)

for i in range(0, avg+1, 1):
    T = 0
    
    for j in range(N):
        for k in range(M):
            if fieldMap[j][k] < i:
                T += put_block(i - fieldMap[j][k])
            
            elif fieldMap[j][k] > i:
                T += remove_block(fieldMap[j][k] - i)
            
            else:
                pass
    
    if T < answer[0]:
        answer = [T, i]
    elif T == answer[0] and i > answer[1]:
        answer = [T, i]
    else:
        pass
    
print(answer[0], answer[1])





#for i in fieldMap:
#    mx = max(i)
#    mn = min(i)
#    
#    if highMax < mx:
#        highMax = mx
#    if highMin > mn:
#        highMin = mn
#
#for j in range(highMax, highMin -1, -1):
#    stackCount = 0
#    removeCount = 0
#    BCount = B
#    
#    for k in fieldMap:
#        for l in k:
#            if l < j:
#                stackCount += j - l
#            elif l > j:
#                removeCount += l - j
#                BCount += 1
#    
#    if len(answer) == 0 and BCount >= stackCount:
#        answer.append(stackCount + removeCount * 2)
#        answer.append(j)
#    elif len(answer) != 0 and BCount >= stackCount:
#        if answer[0] > stackCount + removeCount * 2:
#            answer[0] = stackCount + removeCount * 2
#            answer[1] = j
#        elif answer[0] == stackCount + removeCount * 2:
#            if answer[1] < j:
#                answer[1] = j
#                
#print(answer[0], answer[1])