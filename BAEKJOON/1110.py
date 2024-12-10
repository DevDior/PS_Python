# Clear
# 더하기 사이클

from sys import stdin

A = stdin.readline()

A = int(A)
B = A
count = 0

while True:
    if B < 10:
        B = B*10 + B
        count += 1

    else:
        B = str(B)
        if int(B[0]) + int(B[1]) >= 10:
            B = (int(B[1]) * 10) + int(str(int(B[0]) + int(B[1]))[1])
            count += 1
        else:
            B = (int(B[1]) * 10) + int(str(int(B[0]) + int(B[1]))[0])
            count += 1

    if A == B:
        break

print(count)
