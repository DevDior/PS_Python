# 순열의 순서
import sys, math
from collections import deque

def find_num(n, k):
  num_list = list(range(1, n + 1))
  answer = []

  while True:
    n -= 1
    if k == 1:
      answer = answer + num_list
      print(*answer)
      break
    else:
      _range = math.factorial(n)
      idx = math.ceil(k / _range) - 1
      answer.append(num_list.pop(idx))
      k -= _range * idx


def find_k(n, deq):
  k = 0
  num_list = list(range(1, n + 1))

  for num in deq:
    n -= 1
    _range = math.factorial(n)
    idx = num_list.index(num)
    num_list.pop(idx)
    k += _range * idx

  print(k + 1)


input = sys.stdin.readline

n = int(input())
deq = deque(map(int, input().split()))

p_num = deq.popleft()

if p_num == 1:
  k = deq.pop()
  find_num(n, k)
else:
  find_k(n, deq)