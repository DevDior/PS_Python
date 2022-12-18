# 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, sys.stdin.readline().split())

# 리스트 풀이
book = []

for i in range(N):
    book.append(sys.stdin.readline().rstrip())

for j in range(M):
    try:
        input = sys.stdin.readline().rstrip()
        num = int(input)
        print(book[num-1])
        
    except ValueError:
        print(book.index(input) + 1)
        
# Dictionary 풀이 Hash 자료구조 사용 N(1)