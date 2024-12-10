# Clear
# 알파벳 찾기

import sys

word = sys.stdin.readline()
abc_list = [-1 for i in range(26)]

for i in range(len(word)-1):
    if(abc_list[ord(word[i])-97] == -1):
        abc_list[ord(word[i])-97] = i

for j in abc_list:
    print(j, end=" ")