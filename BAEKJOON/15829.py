# V
# Hashing

import sys

L = int(sys.stdin.readline())
input = sys.stdin.readline()
answer = 0

for i in range(L):
    answer += (ord(input[i]) - 96)*(31**i)
    
print(answer%1234567891)