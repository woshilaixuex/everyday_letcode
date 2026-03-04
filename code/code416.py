from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        maxNum = max(nums)
        half = total // 2
        if n <= 1 or total % 2 != 0:
            return False
        if maxNum > half:
            return False
        dp = [[False] * (half+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True # 初始化第一个数
        for i in range(1,n):
            num = nums[i]
            for j in range(1,half+1):
                if num < j:
                    dp[i][j] = dp[i-1][j-num] or dp[i-1][j] # 选与不选，True是表示可以存在这种集合和为j
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][half]