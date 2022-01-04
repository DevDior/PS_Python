# 괄호

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    vps = list(sys.stdin.readline().strip())
    open = 0
    close = 0
    i = 0
    
    while i < len(vps):
        if vps[i] == '(':
            open += 1
        else:
            close += 1
        
        if open < close:
            break
        
        i += 1
        
    if open == close:
        print('YES')
    else:
        print('NO')