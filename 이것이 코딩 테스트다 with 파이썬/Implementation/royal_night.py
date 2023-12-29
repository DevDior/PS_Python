import sys

input = sys.stdin.readline

p = input()
x = int(p[1])
y = p[0]

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

count = 0 
for i in range(8):
    nx = x + dx[i]
    ny = ord(y) + dy[i]
    
    if nx < 1 or nx > 8 or ny < ord('a') or ny > ord('h'):
        continue
    
    count += 1
    
print(count)