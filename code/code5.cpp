#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size(),left = 0,maxlen = 1;
        vector<vector<bool>> dp(n,vector<bool>(n));
        for (auto i = 0;i < n;i++) dp[i][i] = true;
        for (auto len = 2;len <= n;len++) {
            for (auto i = 0;i < n;i++) {
                int j = i + len - 1;
                if (j >= n) break;
                if (s[i] == s[j]) {
                    if (len == 2) {
                        dp[i][j] = true;
                    }else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                if (dp[i][j] && maxlen < len) {
                    left = i;
                    maxlen = len;
                }
            }
        }
        return s.substr(left,maxlen);
    }
};
int main() {
    Solution solution;
    string s = "cbbd";
    string ans = solution.longestPalindrome(s);
    cout << ans << endl;
}