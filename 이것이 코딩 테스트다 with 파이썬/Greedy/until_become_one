import sys

input = sys.stdin.readline

n, k = map(int, input().split())

count = 0
while True:
  count += 1
  if n % k == 0:
    n = n // k
  else:
    n -= 1

  if n == 1:
    break

print(count)
