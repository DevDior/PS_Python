# V
# IOIOI

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

search_string = 'I' + 'OI' * N
match_count = 0
i = 0
n_count = 0

while i < M - 2:
    if S[i:i+3] == 'IOI':
        i += 2
        n_count += 1
        
        if n_count == N:
            match_count += 1
            n_count -= 1
    else:
        i += 1
        n_count = 0

print(match_count)