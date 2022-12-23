# 1, 2, 3 더하기
import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    dt = [1, 2, 4]
    
    for j in range(3, n):
        dt.append(dt[j-3]+dt[j-2]+dt[j-1])
    
    print(dt[n-1]) 
    
    