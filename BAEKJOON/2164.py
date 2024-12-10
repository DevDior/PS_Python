# Clear
# 카드2

import sys

N = int(sys.stdin.readline())
card = [x for x in range(1, N+1)]

while len(card) != 1:
    if len(card)%2 == 0:
        card = [card[x] for x in range(1, len(card), 2)]
    else:
        card = [card[x] for x in range(1, len(card), 2)]
        card.append(card.pop(0))
    
print(card[0])