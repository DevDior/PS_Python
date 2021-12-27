# v

import sys

n1, n2 = map(int, sys.stdin.readline().split())
if n1 > n2:
    n1, n2 = n2, n1
    
if n1 <= n2:
    for i in range(n1, 0, -1):
        if n1 % i == 0:
            answer1 = i
            
            if n2 % answer1 == 0:
                print(answer1)
                break

key = int(n2//answer1)
print(n1*key)