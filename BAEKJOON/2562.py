from sys import stdin

max = int(stdin.readline())
count = 1

for i in range(8):
    tmp = int(stdin.readline())
    if tmp > max:
        max = tmp
        count = i + 2
print(max)
print(count)