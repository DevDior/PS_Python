# Clear
# A+B - 4

from sys import stdin

while True:
    try:
        A, B = map(int, stdin.readline().split())
        print(A + B)
    except:
        break