# Clear
# 음계

import sys

nums = sys.stdin.readline().split()
numLen = len(nums)
mixed = False

for i in range(numLen):
    nums[i] = int(nums[i])

if(nums[0] ==1):
    for _ in range(1, numLen):
        if(nums[_] - nums[_-1] != 1):
            print("mixed")
            mixed = True
            break
    if(mixed ==False) : print("ascending")
elif(nums[0] == 8):
    for _ in range(1, numLen):
        if(nums[_] - nums[_-1] != -1):
            print("mixed")
            mixed = True
            break
    if(mixed == False): print("descending")
else:
    print("mixed")