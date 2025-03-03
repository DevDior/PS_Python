import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    inputs = input().split()
    array.append((inputs[0], int(inputs[1])))

array.sort(key = lambda x: x[1])

for i in array:
    print(i[0], end=' ')