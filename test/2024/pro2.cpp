#include <bits/stdc++.h>
using namespace std;

int m,n;
vector<bool> used;
void dfs(int start,vector<int>& temp){
    if (temp.size() == n) {
        for (auto x : temp) cout << x << " ";
        cout << endl;
        return;
    }
    for (auto i = 0;i < m;i++) {
        if (used[i]) continue;;
        used[i] = true;
        temp.push_back(i+1);
        dfs(i+1,temp);
        used[i] = false;
        temp.pop_back();
    }
}
int main() {
    cin >> m >> n;
    vector<int> temp;
    used.resize(m, false);
    dfs(0,temp);
}
// 64 位输出请用 printf("%lld")