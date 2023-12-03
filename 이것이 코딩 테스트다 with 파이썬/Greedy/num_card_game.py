import sys

input = sys.stdin.readline

n, m = map(int, input().split())
card_list = [list(map(int, input().split())) for i in range(n)]

answer = 0
for row in card_list:
  smallest_num = min(row)
  if smallest_num > answer:
    answer = smallest_num

print(answer)