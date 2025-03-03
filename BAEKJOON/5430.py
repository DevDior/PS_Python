# Clear
# AC

import sys
from collections import deque
input = sys.stdin.readline


def func_d(queue: deque, flag_r: bool):
    if not queue:
        return "error"
    else:
        if flag_r:
            queue.pop()
        else:
            queue.popleft()
        return queue

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    input_data = input()
    queue = deque()
    
    if n == 0:
        pass
    else:
        queue = deque(list(map(int, input_data.rstrip()[1:-1].split(','))))
    
    raise_error = False
    flag_r = False
    for func in p:
        if func == 'R':
            flag_r = not flag_r
        elif func == 'D':
            result = func_d(queue, flag_r)
            if result == 'error':
                raise_error = True
                break
            else:
                queue = result
    
    if raise_error == True:
        print('error')
    else:
        if flag_r:
            queue.reverse()
            print(str(list(queue)).replace(' ', ''))
        else:
            print(str(list(queue)).replace(' ', ''))