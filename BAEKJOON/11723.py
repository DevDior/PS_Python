# 집합

import sys

def add(S, x):
    if not x in S:
        S.add(x)

def remove(S, x):
    S.discard(x)
    
def check(S, x):
    if x in S:
        print(1)
    else:
        print(0)
        
def toggle(S, x):
    try:
        S.remove(x)
        
    except KeyError:
        S.add(x)

def all(S):
    S = {i for i in range(1, 21)}
    return S

def empty(S):
    S = set()
    return S

S = set()
M = int(sys.stdin.readline())

for i in range(M):
    list_command = list(sys.stdin.readline().split())
    command = list_command[0]
    if not command in ['all', 'empty']:
        num = int(list_command[1])
    
    if command == 'add':
        add(S, num)
    elif command == 'remove':
        remove(S, num)
    elif command == 'check':
        check(S, num)
    elif command == 'toggle':
        toggle(S, num)
    elif command == 'all':
        S = all(S)
    else:
        S = empty(S)