# 패션왕 신해빈
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    clothes = dict()
    answer = 1
    
    for i in range(n):
        value, key = map(str, sys.stdin.readline().split())
        if key in clothes:
            value_list = clothes[key]
            value_list.append(value)
            clothes[key] = value_list
        else:
            clothes[key] = [value]
    
    for j in clothes:
        answer *= len(clothes[j]) + 1
    
    print(answer -1)