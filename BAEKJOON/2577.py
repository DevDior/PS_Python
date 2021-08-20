from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())

result = A * B * C
answerList = [0 for i in range(10)]

result = str(result)
for i in result:
    if i == '0':
        answerList[0] += 1
    elif i == '1':
        answerList[1] += 1
    elif i == '2':
        answerList[2] += 1
    elif i == '3':
        answerList[3] += 1
    elif i == '4':
        answerList[4] += 1
    elif i == '5':
        answerList[5] += 1
    elif i == '6':
        answerList[6] += 1
    elif i == '7':
        answerList[7] += 1
    elif i == '8':
        answerList[8] += 1
    else:
        answerList[9] += 1

for j in answerList:
    print(j)
