# Clear
# 체스판 다시 칠하기

import sys

def check_change(board2):
    c = 0
    if board2[0][0] == 'W':
        for k in range(8):
            for l in range(8):
                if k%2 == 0:
                    if l%2 == 0:
                        if board2[k][l] != 'W':
                            c += 1
                    elif l%2 == 1:
                        if board2[k][l] != 'B':
                            c += 1
                elif k%2 == 1:
                    if l%2 == 0:
                        if board2[k][l] != 'B':
                            c += 1
                    elif l%2 == 1:
                        if board2[k][l] != 'W':
                            c += 1
    elif board2[0][0] == 'B':
        for k in range(8):
            for l in range(8):
                if k%2 == 0:
                    if l%2 == 0:
                        if board2[k][l] != 'B':
                            c += 1
                    elif l%2 == 1:
                        if board2[k][l] != 'W':
                            c += 1
                            
                elif k%2 == 1:
                    if l%2 == 0:
                        if board2[k][l] != 'W':
                            c += 1
                    elif l%2 == 1:
                        if board2[k][l] != 'B':
                            c += 1
    return c

N, M = map(int, sys.stdin.readline().split())
board = []
change = 2499

for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

for i in range(N-7):
    for j in range(M-7):
        board2 = []
        
        for n in range(8):
            board2.append(board[i+n][j:j+8])
        
        a = check_change(board2)
        
        if board2[0][0] == 'W':
            board2[0][0] = 'B'
        else:
            board2[0][0] = 'W'
        b = check_change(board2) + 1
        
        if a < b:
            if change > a:
                change = a
        else:
            if change > b:
                change =b 
            
print(change)