# Clear
# 듣보잡

import sys

N, M = map(int, sys.stdin.readline().split())
ansewr = 0
answer_list = []
not_see = set()

for i in range(N):
    not_see.add(sys.stdin.readline().rstrip())
    
for j in range(M):
    not_hear = sys.stdin.readline().rstrip()
    if not_hear in not_see:
        ansewr += 1
        answer_list.append(not_hear)
        
print(ansewr)
answer_list.sort()
for k in answer_list:
    print(k)