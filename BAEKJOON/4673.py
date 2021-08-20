# 셀프 넘버

import sys

def d(n):
    if n <10:
        n = n + n
    elif n < 100:
        n = n + n//10 + n%10
    elif n < 1000:
        n = n + n//100 + (n%100)//10 + (n%100)%10
    elif n < 10000:
        n = n + n//1000 + (n%1000)//100 + ((n%1000)%100)//10 + (((n%1000))%100)%10
    return n

a = set()
for i in range(1, 10000):
    a.add(d(i))
    if i not in a:
        print(i)