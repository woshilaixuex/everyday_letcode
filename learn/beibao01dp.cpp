/**
 * https://www.luogu.com.cn/problem/P2871
 */
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n = 0,m = 0;
    cin >> n >> m ;
    vector<int> w(n,0);
    vector<int> d(n,0);
    for (auto i = 0;i < n;i++) {
        cin >> w[i] >> d[i];
    }
    vector<int> dp(m+1,0);
    for (auto i = 0;i < n;i++) {
        for (auto j = m;j >= w[i];j--) {
            dp[j] = max(dp[j],dp[j-w[i]] + d[i]); 
        }
    }
    cout << dp[m] << endl;
}