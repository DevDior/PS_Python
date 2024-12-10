# Clear
# 잃어버린 괄호

from itertools import count
import sys

formula = sys.stdin.readline().rstrip()
count_list = formula.split('-')
answer = 0

for _ in range(len(count_list)):
    unit_sum = 0
    unit_list = count_list[_].split('+')
    
    for i in unit_list:
        c = 0
        while i[c] == 0:
            c += 1
            
        unit_sum += int(i[c:])
    
    if _ == 0:
        answer += unit_sum
        
    else:
        answer -= unit_sum
        
print(answer)