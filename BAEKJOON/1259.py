# Clear
# 팰린드롬수

import sys

while True:
    answer = True
    s = 0
    e = -1
    
    pld = sys.stdin.readline().strip()
    
    if pld == '0':
        break
    
    if len(pld) %2 == 0:
        while s < len(pld)//2:
            if pld[s] != pld[e]:
                answer = False
                break
            s += 1
            e -= 1
            
    else:
        while s < len(pld)//2:
            if pld[s] != pld[e]:
                answer = False
                break
            s += 1
            e -= 1

    if answer == True:
        print('yes')
    else:
        print('no')
        