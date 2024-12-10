# Clear
# 2xN 타일링

import sys
n = int(sys.stdin.readline())
answer_list = [1, 2]

for i in range(2, n):
    answer_list.append(sum(answer_list[i-2:i]))

print(answer_list[n-1]%10007)