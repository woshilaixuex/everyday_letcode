#include<bits/stdc++.h>
using namespace std;
class Solution {
    unordered_map<char,int> smp,tmp;
public:
    bool check(){
        for (auto const &tv:tmp) {
            if (smp[tv.first] < tv.second) return false;
        }
        return true;
    }
    string minWindow(string s, string t) {
        int n = s.size(),m = t.size();
        if (n < m) return ""; 
        for (auto const &c: t) {
            ++tmp[c];
        }
        int left = 0,right = -1;
        int len = INT_MAX;
        int ansL = -1,ansR = -1;
        while (right < n) {
            if (tmp.find(s[++right]) != tmp.end()) {
                ++smp[s[right]];
            }
            while (check()&&left <= right){
                if (right-left+1 < len) {
                    ansL = left;
                    ansR = right;
                    len = right-left+1;
                }
                if (tmp.find(s[left]) != tmp.end()) {
                    --smp[s[left]];
                }
                ++left;
            }
        }
        return ansL == -1 ? string() : s.substr(ansL, len);
    }

};
int main() {
    Solution solution;
    string s = "ADOBECODEBANC";
    string t = "ABC";
    string ans = solution.minWindow(s,t);
    cout << ans << endl;
}