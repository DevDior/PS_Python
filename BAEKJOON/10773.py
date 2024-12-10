# Clear
# 제로

import sys
K = int(sys.stdin.readline())

answer = []

for i in range(K):
    answer.append(int(sys.stdin.readline()))
    if answer[-1] == 0:
        answer.pop(-1)
        answer.pop(-1)

print(sum(answer))