#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    /**
     *  i,j是w1，w2前i,j个字母平衡时的编辑距离，所以只需要考虑i-1,j i,j-1以及i-1,j-1时的状态，操作分别是w1添加，w2添加，以及w1或w2修改最后的字母
     */
    int minDistance(string word1, string word2) {
        int l1 = word1.size();
        int l2 = word2.size();
        vector<vector<int>> dp(l1+1,vector<int>(l2+1));
        for (auto i = 0;i <= l1;i++) dp[i][0] = i;
        for (auto i = 0;i <= l2;i++) dp[0][i] = i;
        for (auto i = 1;i <= l1;i++) {
            for (auto j = 1;j <= l2;j++) {
                if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = min(dp[i-1][j-1]-1,min(dp[i][j-1],dp[i-1][j]))+1;
                }else {
                    dp[i][j] = min(dp[i-1][j-1],min(dp[i][j-1],dp[i-1][j]))+1;
                }
            }
        }
        return dp[l1][l2];
    }
};
int main() {
    Solution solution;
    string word1 = "horse",word2 = "ros";
    int x = solution.minDistance(word1,word2);
    cout << x << endl;
}