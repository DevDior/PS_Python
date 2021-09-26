# 상수
import sys

nums = sys.stdin.readline().split()

if(nums[0][::-1] > nums[1][::-1]): print(nums[0][::-1])
else: print(nums[1][::-1])