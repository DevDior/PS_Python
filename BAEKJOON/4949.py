# Clear
# 균형잡힌 세상

import sys

while True:
    string = sys.stdin.readline().rstrip()
    compareList = []
    answer = True
    
    for i in string:
        if i == '(' or i == '[':
            compareList.append(i)
        elif i == ')':
            if len(compareList) == 0 or compareList.pop(-1) != '(':
                print('no')
                answer = False
                break
        elif i == ']':
            if len(compareList) == 0 or compareList.pop(-1) != '[':
                print('no')
                answer = False
                break
            
    if len(string) == 1 and string == '.':
        break
    elif len(compareList) != 0 and answer == True:
        print('no')
    elif answer == True:
        print('yes')