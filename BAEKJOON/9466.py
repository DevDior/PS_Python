# 텀 프로젝트
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(n, m):
    sn = select_list[n]
    
    if n == sn-1:
        joined_list[sn-1] = 2
        stack.pop()
        return -1, None
    
    elif joined_list[sn-1] == 0:
        stack.append(sn-1)
        joined_list[sn-1] = 1
        joined_value, tn = dfs(sn-1, m)
        joined_list[n] = joined_value
        
        if tn == None:
            return joined_value, tn
        else:
            stack.pop()
            if joined_value == 2 and n != tn:
                return joined_value, tn
            elif joined_value == 2 and n == tn:
                return -1, None
    
    elif joined_list[sn-1] == 2:
        joined_list[n] = -1
        return -1, None
    
    elif joined_list[sn-1] == 1:
        stack.pop()
        joined_list[n] = 2
        return 2, sn-1
    
    elif joined_list[sn-1] == -1:
        joined_list[n] = -1
        return -1, None


T = int(input())
for _ in range(T):
    n = int(input())
    select_list = list(map(int, input().split()))
    # -1: 팀 결성 실패, 0: 기본 값, 1: 팀 선택 중, 2: 이미 팀 결성
    joined_list = [0] * n
    stack = []
    for i in range(n):
        if joined_list[i] == 0:
            stack.append(i)
            joined_list[i] = 1
            dfs(i, n)
    
    print(len(stack))