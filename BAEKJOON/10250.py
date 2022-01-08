# ACM 호텔 can't solve
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    a = N%H
    if a == 0:
        a = H
        
    b = N//H
    if b == N/H:
        b -= 1
        
    b += 1 
    answer = a*100 + b
    print(answer)