# 팩토리얼 0의 개수
import sys

N = int(sys.stdin.readline())
final_num = 1
answer = 0

for i in range(N, 0, -1):
    final_num *= i

str_final_num = str(final_num)

for j in range(len(str_final_num)-1, -1, -1):
    if str_final_num[j] == '0':
        answer += 1
    else:
        break;

print(answer)