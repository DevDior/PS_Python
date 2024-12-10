# V
# 영화감독 숌

import sys

N = int(sys.stdin.readline())

num = 666

for i in range(1, N):
    num += 1
    
    while ('666' in str(num)) == False:
        num += 1
    
print(num)