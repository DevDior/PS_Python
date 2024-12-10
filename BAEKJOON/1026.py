# Clear
# 보물

import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

result = 0
for i in range(n):
  result += a_list[i] * b_list[i]

print(result)