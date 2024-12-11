# V
# 투에-모스 문자열

"""
1. 아이디어 
2^n < k <= 2^(n+1)인 2^(n+1)값 찾기
k의 값은 k - 2^(n+1) // 2 값의 반대
위 로직 재귀함수로 구현(매개변수 1일 경우 0 반환, 2일 경우 1 반환)

2. 시간 복잡도
- O(logN)

3. 자료구조
return: int
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())

def circulate(k: int):
    if k == 1:
        return 0
    if k == 2:
        return 1
    
    end = next_power_of_two(k)
    
    mid = end // 2
    
    _k = k - mid
    
    if circulate(_k) == 0:
        return 1
    else:
        return 0

def next_power_of_two(k):
    if k & (k - 1) == 0:    # 2의 거듭제곱인지 확인
        return k
    return 2 ** k.bit_length()  # 상위 2의 거듭제곱 계산

print(circulate(k))