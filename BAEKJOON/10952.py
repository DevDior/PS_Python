# 10952번 : A+B - 5

from sys import stdin

while True:
    A, B = map(int, stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)
