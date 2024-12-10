# V
# 큐

import sys

N = int(sys.stdin.readline())
Queue = []

for _ in range(N):
    com = sys.stdin.readline().split()
    
    if com[0] == 'push':
        Queue.append(int(com[1]))
    elif com[0] == 'pop':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue.pop(0))
    elif com[0] == 'size':
        print(len(Queue))
    elif com[0] == 'empty':
        if len(Queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])
    elif com[0] == 'back':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[-1])