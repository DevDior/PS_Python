import sys
import math

def custom_round(n):
    if n - math.floor(n) >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)

opinion_num = int(sys.stdin.readline())
difficulty_list = sorted([int(sys.stdin.readline()) for _ in range(opinion_num)])

erase_count = custom_round(opinion_num*0.15)

if opinion_num == 0:
    print(0)
elif erase_count == 0:
    print(custom_round(sum(difficulty_list[erase_count:])/(opinion_num-erase_count*2)))
else:
    print(custom_round(sum(difficulty_list[erase_count:erase_count*-1])/(opinion_num-erase_count*2)))