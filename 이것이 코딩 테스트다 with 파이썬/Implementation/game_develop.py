import sys
input = sys.stdin.readline

def turn_left(d):
    if d == 0:
        return 3
    else:
        return d - 1

def go_back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    else:
        return 1

N, M = map(int, input().split())
x, y, d = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, +1, 0, -1]
ground = [input().split() for i in range(N)]    # 0, 1, 2 = 방문x, 바다, 방문o
ground[x][y] = '2'
visit_cnt = 1

b = True
while b:
    for i in range(4):
        d = turn_left(d)
        nx = x + dx[d]
        ny = y + dy[d]
        
        if ground[nx][ny] == '0':
            x = nx
            y = ny
            ground[nx][ny] = '2'
            visit_cnt += 1
            break
        else:
            if i == 3:
                n = go_back(d)
                x = x + dx[n]
                y = y + dy[n]
                
                if ground[x][y] == '1':
                    b = False
                    break
print(visit_cnt)
                
    
