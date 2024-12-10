# Clear
# 검증수

import sys

nums = sys.stdin.readline().split()

totalSub = 0

for i in range(len(nums)):
    totalSub += int(nums[i])**2

print(totalSub%10)