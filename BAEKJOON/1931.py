# 회의실 배정
import sys

N = int(sys.stdin.readline())
discuss_time = [tuple(map(int, sys.stdin.readline().split())) for x in range(N)]
discuss_time.sort(key=lambda x: (x[1], x[0]))
discuss = discuss_time[0]
discuss_count = 1

for i in range(1, N):
    if discuss_time[i][0] >= discuss[1]:
        discuss = discuss_time[i]
        discuss_count += 1

print(discuss_count)