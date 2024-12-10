# Clear
# 평균은 넘겠지

import sys

C = int(sys.stdin.readline())

for i in range(C):
    total_list = list(map(int, sys.stdin.readline().split()))
    N = total_list[0]
    score_list = total_list[1:]

    avg = sum(score_list)/N
    high_student = 0

    for j in range(N):
        if score_list[j] > avg:
            high_student += 1

    high_student_value = round((high_student/N)*100, 3)
    
    # 이 부분은 f-string formating으로 해결 가능
    print("%0.3f" %(high_student_value), end='')
    print('%')