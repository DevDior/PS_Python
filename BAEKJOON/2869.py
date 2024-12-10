# Clear
# 달팽이는 올라가고 싶다

import sys

A, B, V = map(int ,sys.stdin.readline().split())

V -= A
b = A-B
day = 1

c = V//b
if V/b > c:
    c += 1
    
day = day + c
print(day)