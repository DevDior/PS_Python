# Clear
# 직삼각형

import sys

while(True):
    nums = list(map(int, sys.stdin.readline().split()))
    if(nums == [0, 0, 0]): break

    maxNum = max(nums)
    nums.remove(maxNum)

    if(maxNum**2 == nums[0]**2 + nums[1]**2): print("right")
    else: print("wrong")