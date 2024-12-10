# Clear
# A+B - 8

import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'%(i+1, A, B, A+B))