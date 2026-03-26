#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, n;
int f[200001];
vector< pair<int, pair<int, int> > >  s_n(200001);
int dp[200001][3];//0-r 1-g 2-b
string s;

pair<int, pair<int, int> > Switch(char a){
    if(a == 'r') return {0, {1, 2}} ;
    else if (a == 'g') return {1, {0, 2}};
    return {2, {0, 1}};
}

int main(){
    cin >> N;
    while(N --){
        cin >> n;
        cin >> s;
        for(int i = 0;i < n;i ++)
            s_n[i] = Switch(s[i]);
        for(int i = 0;i < n;i ++){
            cin >> f[i];
            int j = s_n[i].second.first, k = s_n[i].second.second;
            if (i){
                dp[i][s_n[i].first] = min(dp[i-1][j], dp[i-1][k]);
                dp[i][j] = min(dp[i-1][s_n[i].first]+f[i], dp[i-1][k]+f[i]);
                dp[i][k] = min(dp[i-1][s_n[i].first]+f[i], dp[i-1][j]+f[i]);
            }else {
                dp[i][s_n[i].first] = 0;
                dp[i][j] = f[i], dp[i][k] = f[i];
            }
        }
        cout << min( min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]) << endl;
    }

    return 0;
}