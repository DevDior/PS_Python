# Clear
# 알람시계

import sys

H, M = map(int, sys.stdin.readline().split())

if M >= 45:
    print(H, M-45)
elif H > 0:
    print(H-1, M + 15)
else:
    print(23, M + 15)