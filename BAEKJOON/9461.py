# 파도반 수열
import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    p_list = [1, 1, 1, 2, 2]
    
    if N < 5:
        print(p_list[N-1])
    
    else:
        for i in range(5, N):
            p_list.append(p_list[-1]+p_list[i-5])
        
        print(p_list[-1])