#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int atMostNGivenDigitSet(vector<string>& digits, int n) {
        string s = to_string(n);
        int k = s.size();
        int m = digits.size();
        vector<vector<int>> dp(k+1,vector<int>(2));
        dp[0][1] = 1;
        for (auto i = 1;i <= k;i++) {
            for (auto j = 0;j < m;j++) {
                if (digits[j][0] < s[i-1]) {
                    dp[i][0] += dp[i-1][1];
                }else if (digits[j][0] == s[i-1]) {
                    dp[i][1] = dp[i-1][1];
                }else {
                    break;
                }
            }
            if (i > 1) {
                dp[i][0] += m + dp[i-1][0] * m;
            }
        }
        return dp[k][0] + dp[k][1];
    }
};
int main() {
    Solution solution;
    int n = 100;
    vector<string> digits = {"1","3","5","7"};
    int ans = solution.atMostNGivenDigitSet(digits,n);
    cout << ans << endl;
}