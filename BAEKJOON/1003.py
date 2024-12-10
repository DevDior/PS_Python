# Clear
# 피보나치 함수
import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    answer = [0, 1]
    past_answer = [1, 0]
    
    if N == 0:
        print(1, 0)
        
    elif N == 1:
        print(0, 1)
        
    else:
        for j in range(1, N):
                tmp = answer
                answer = [answer[0]+past_answer[0], answer[1]+past_answer[1]]
                past_answer = tmp
         
        print(answer[0], answer[1])