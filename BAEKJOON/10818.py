# Clear
# 최소, 최대

from sys import stdin

N = int(stdin.readline())
lineList = list(map(int, stdin.readline().split()))

max = lineList[0]
min = lineList[0]

for i in lineList:
    if i > max:
        max = i
    if i < min:
        min = i

print(min, max)