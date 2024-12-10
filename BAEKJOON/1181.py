# Clear
# 단어 정렬

import sys

wordList = []

N = int(sys.stdin.readline())
for i in range(N):
    word = sys.stdin.readline().strip()
    if(word in wordList):
        pass
    else:
        wordList.append(word)

wordList.sort(key = lambda x: (len(x), x))

for j in wordList:
    print(j)