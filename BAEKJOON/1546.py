# Clear
# 평균

import sys

N = int(sys.stdin.readline())

s = list(map(int, sys.stdin.readline().split()))
s_max = max(s)

for i in range(N):
    s[i] = (s[i]/s_max)*100

avg = sum(s)/len(s)
print(avg)