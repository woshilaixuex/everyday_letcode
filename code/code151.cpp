#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        int n = s.size();
        int curr = n-1;
        while (curr > 0&&s[curr] == ' ') curr--;
        int r = curr;
        while (curr >= 0) {
            while(curr >= 0&&s[curr] != ' ') curr--;
            ans += s.substr(curr+1,r-curr) + " ";
            while(curr >= 0&&s[curr] == ' ') curr--;
            r = curr;
        }
        return ans.substr(0,ans.size()-1);
    }
};
int main() {
    Solution solution;
    string s = "the sky is blue";
    string ans = solution.reverseWords(s);
    cout << ans << endl;
}