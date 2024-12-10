# Clear
# 과일 탕후루

import sys
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))
start = 0
end = 0
answer = 0
now_kinds = dict()

# 투 포인터 알고리즘 사용
while end < N:
    if len(now_kinds) < 2 or fruits[end] in now_kinds.keys():
        if fruits[end] in now_kinds.keys():
            now_kinds[fruits[end]] += 1
        else:
            now_kinds[fruits[end]] = 1
        
        if answer < end + 1 - start:
            answer = end + 1 - start
        
        end += 1
    else:
        now_kinds[fruits[start]] -= 1
        if now_kinds[fruits[start]] == 0:
            now_kinds.pop(fruits[start])
        
        start += 1
    
print(answer)