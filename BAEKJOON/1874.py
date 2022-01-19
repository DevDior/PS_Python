# 스택 수열

import sys

n = int(sys.stdin.readline())
sequence = []
stack = []
answer = []

for _ in range(n):
    sequence.append(int(sys.stdin.readline()))

c = 1
minusCount = 0
offset = 0

while minusCount != n:
    if c == sequence[offset]:
        answer.append('+')
        answer.append('-')
        minusCount += 1
        offset += 1
        c += 1
    elif c > sequence[offset]:
        if stack.pop(-1) == sequence[offset]:
            answer.append('-')
            minusCount += 1
            offset += 1
        else:
            print('NO')
            break
    else:
        stack.append(c)
        answer.append('+')
        c += 1

if minusCount == n:
    for i in answer:
        print(i)