# Clear
# 벌집

from sys import stdin

N = int(stdin.readline())

if N == 1:
    print(1)
else:
    sum = 7
    i = 2
    while sum < N:
        sum += 6 * i
        i += 1
    print(i)
