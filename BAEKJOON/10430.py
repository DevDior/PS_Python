# 10430번 : 나머지

from sys import stdin

A, B, C = map(int, stdin.readline().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
