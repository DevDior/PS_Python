# 설탕 배달

import sys

N = int(sys.stdin.readline())

f = N//5
t = -1

for i in range(f, -1, -1):
    n = N-i*5
    if n%3 == 0:
        f = i
        t = n//3
        break

if t != -1:
    print(f+t)
else:
    print(t)