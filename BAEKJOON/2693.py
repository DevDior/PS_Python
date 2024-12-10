# Clear
# N번째 큰 수

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    
    A = list(map(int, sys.stdin.readline().split()))
    m = 0
    i = 0
    # 버블 정렬
    while(1):
        if (A[i] > A[i+1]):
            tmp = A[i]
            A[i] = A[i+1]
            A[i+1] = tmp
            m = 1
            if ( i < 8 ):
                i += 1
        elif (((A[i] <= A[i+1]) or i == 9) and m == 1):
            i = 0
            m = 0
        else:
            i += 1
        if (i == 9 and m == 0):
            break;
        
    print(A[7])