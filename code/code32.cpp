#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        vector<int> dp(n+1,0);
        int ans = 0;
        // (())()
        for (auto i = 1;i < n;i++) {
            if (s[i] == ')') {
                if (s[i-1] == '(') {
                    dp[i] = 2;
                }
                if (dp[i-1] != 0&&i-dp[i-1]-1 >= 0&&s[i-dp[i-1]-1] == '(') {
                    dp[i] = dp[i-1] + 2;
                }
                if (i-dp[i] >= 0&&dp[i-dp[i]] != 0) {
                    dp[i] = dp[i] + dp[i-dp[i]];
                }
                ans = max(ans,dp[i]);
            }
        }
        return ans;
    }
};
int main(){
    string s = "()(())";
    Solution solution;
    int ans = solution.longestValidParentheses(s);
    cout << ans << endl;
}