# Clear
# 별 찍기 - 2

import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    print(' ' * (N-i), end='*' * i + '\n')