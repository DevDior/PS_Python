import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(n):

    if n == 0:
        return 1

    a = 1

    while n > 0:
        a *= n
        n -= 1
    
    return a

print(factorial(N)//(factorial(K)*factorial(N-K)))