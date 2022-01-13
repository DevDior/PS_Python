# 덩치

import sys

N = int(sys.stdin.readline())
group = []
answer = [0 for x in range(N)]

for _ in range(N):
    group.append(tuple(map(int, sys.stdin.readline().split())))

rank = 1
count = 1

while max(group)[1] != 0:
    inform = max(group)
    index = group.index(inform)
    group[index] = (0, 0)
    answer[index] = rank
    count += 1
    
    for j in range(N):
        if inform[1] < group[j][1] or inform == group[j]:
            index2 = group.index(group[j])
            group[j] = (0, 0)
            answer[index2] = rank
            count += 1
    
    rank = count
    
for j in range(len(answer)):
    if j != len(answer)-1:
        print(answer[j], end=' ')
    else:
        print(answer[j])