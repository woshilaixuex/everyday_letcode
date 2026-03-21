#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<int> dp(amount+1,-1);
        dp[0] = 0;
        for (auto i = 1;i <= amount;i++) {
            for (auto j = 0;j < n;j++) {
                if (i - coins[j] >= 0&&dp[i - coins[j]] != -1) {
                    if (dp[i] != -1) {
                        dp[i] = min(dp[i],dp[i - coins[j]] + 1);
                    }else {
                        dp[i] = dp[i - coins[j]] + 1;
                    }
                }
            }
        }
        return dp[amount];
    }
};
int main() {
    Solution solution;
    vector<int> coins {2};
    int ans = solution.coinChange(coins,3);
    cout << ans << endl;
}