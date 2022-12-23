# 바이러스
from collections import deque
import sys


n = int(sys.stdin.readline())
link_list = [list(map(int, sys.stdin.readline().split())) for x in range(int(sys.stdin.readline()))]
dict_link_list = dict()

# list => dict
for i in link_list:
    value = dict_link_list.get(i[0])
    value2 = dict_link_list.get(i[1])
    
    if value == None:
        dict_link_list[i[0]] = [i[1]]
    else:
        value.append(i[1])
        dict_link_list[i[0]] = value
    
    if value2 == None:
        dict_link_list[i[1]] = [i[0]]
    else:
        value2.append(i[0])
        dict_link_list[i[1]] = value2
    
infected_com = [False] * n
infected_com[0] = True
answer = 0

# BFS
queue = deque()
queue.append(1)

while(queue):
    com_num = queue.popleft()
    value = dict_link_list.get(com_num)
    
    if value:
        for i in value:
            if not infected_com[i-1]:
                infected_com[i-1] = True
                answer += 1
                queue.append(i)

print(answer)