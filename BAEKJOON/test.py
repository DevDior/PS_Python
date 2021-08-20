import sys

d = []
d.append([0 for i in range(11)])
for i in range(1, 11):
    d.append(list(map(int, sys.stdin.readline().split())))
    d[i].insert(0, 0)
    
x = y = 2
d[x][y] = 9

while True:
    if d[x][y+1] == 0:
        d[x][y+1] = 9
        y += 1
    elif d[x][y+1] == 1:
        if d[x+1][y] == 0:
            d[x+1][y] = 9
            x += 1
        elif d[x+1][y] == 1:
            break
        else:
            d[x+1][y] = 9
            break
    else:
        d[x][y+1] = 9
        break
        
for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end=' ')
    print()