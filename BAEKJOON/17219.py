# Clear
# 비밀번호 찾기

import sys

N, M = map(int, sys.stdin.readline().split())
dic_account = dict()

for i in range(N):
    id, password = sys.stdin.readline().split()
    dic_account[id] = password

for j in range(M):
    search_id = sys.stdin.readline().rstrip()
    print(dic_account.get(search_id))