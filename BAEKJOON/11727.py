# 2×n 타일링 2
import sys

n = int(sys.stdin.readline())
answer_list = [1, 3]

for i in range(2, n):
    answer_list.append(answer_list[i-1] + answer_list[i-2]*2)
    
print(answer_list[n-1]%10007)