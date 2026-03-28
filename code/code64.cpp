#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size(),m = grid[0].size();
        vector<vector<int>> dp(n,vector<int>(m,0));
        dp[0][0] = grid[0][0];
        for (auto i = 0;i < n;i++) {
            for (auto j = 0;j < m;j++) {
                int dx = i - 1,dy = j - 1;
                if (dx >= 0) dp[i][j] = dp[dx][j]+grid[i][j];
                if (dy >= 0) dp[i][j] = dp[i][dy]+grid[i][j];
                if (dx >= 0&&dy >= 0) dp[i][j] = min(dp[dx][j],dp[i][dy]) + grid[i][j];
            }
        }
        return dp[n-1][m-1];
    }
};
int main() {
    vector<vector<int>> grid = {{1,3,1},{1,5,1},{4,2,1}};
    Solution solution;
    int ans = solution.minPathSum(grid);
    cout << ans << endl;
}