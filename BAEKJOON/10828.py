# Clear
# 스택

import sys

def push(stack, n):
    stack.append(n)
    
def pop(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]
        
def size(stack):
    print(len(stack))
    
def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)
    
def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
    
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        push(stack, int(command[1]))
        
    elif command[0] == "pop":
        pop(stack)
    
    elif command[0] == "size":
        size(stack)
    
    elif command[0] == "empty":
        empty(stack)
    elif command[0] == "top":
        top(stack)