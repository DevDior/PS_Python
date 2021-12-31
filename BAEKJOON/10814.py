# 나이순 정렬 v

import sys

N = int(sys.stdin.readline())

userList = []

for _ in range(N):
    userList.append(sys.stdin.readline().split())
    
userList.sort(key=lambda x:int(x[0]))

for i in range(N):
    print(userList[i][0], end=' ')
    print(userList[i][1])