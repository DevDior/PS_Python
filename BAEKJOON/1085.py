# Clear
# 직사각형 탈출

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if(x >= w/2 and y >= h/2):
    if(w - x <= h - y): print(w - x)
    else: print(h - y)
elif(x < w/2 and y >= h/2):
    if(x <= h -y): print(x)
    else: print(h-y)
elif(x < w/2 and y < h/2):
    if(x <= y): print(x)
    else: print(y)
else:
    if(w - x <= y): print(w - x)
    else: print(y)