# V
# Four Squares

import sys
import math

# DP
n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n+1):
    dp.append(4)
    
    for j in range(int(math.sqrt(i)), 0, -1):
        dp[-1] = min(dp[i-j**2]+1, dp[i-1]+1, dp[-1])
    
print(dp[n])