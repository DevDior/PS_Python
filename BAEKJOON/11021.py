# Clear
# A+B - 7

import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i+1, A+B))