from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for index in range(1,n):
            dp[index][0] = dp[index-1][0] + grid[index][0]
        for index in range(1,m):
            dp[0][index] = dp[0][index-1] + grid[0][index]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j] 
        return dp[n-1][m-1]
if __name__ == "__main__":
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans = solution.minPathSum(grid)
    print(ans)