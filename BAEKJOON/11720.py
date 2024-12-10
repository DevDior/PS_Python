# Clear
# 숫자의 합

import sys

answer = 0
T = int(sys.stdin.readline())
n = sys.stdin.readline()

for i in range(T):
    answer += int(n[i])

print(answer)