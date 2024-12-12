# Clear
# 배열 합치기

"""
1. 아이디어
- 두 리스트 합치고 정렬
- 투 포인터로 풀 수도 있지만, 파이썬의 sort()를 이용하면 간단하게 해결 가능

2. 시간복잡도
- O(NlogN)

3. 자료구조
input: list
return: list
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(" ".join(map(str, sorted(A+B))))