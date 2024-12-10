# V
# 단어 공부

import sys
word = sys.stdin.readline().upper().rstrip()

countAlpabat = list(set(word))
countNums = []

for i in range(len(countAlpabat)):
    countNums.append(word.count(countAlpabat[i]))

if(countNums.count(max(countNums)) > 1): print("?")
else: print(countAlpabat[countNums.index(max(countNums))])