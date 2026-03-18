#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int right = 0;
        int len = s.size();
        unordered_set<char> uset;
        int ans = 0;
        for (int left = 0;left < len;left++) {
            if (left != 0) {
                uset.erase(s[left-1]);
            }
            while (right < len && !uset.count(s[right])) {
                uset.insert(s[right]);
                right++;
            }
            ans = max(ans,int(uset.size()));
        } 
        return ans;
    }
};
int main(){
    Solution solution;
    string s = "abcabcbb";
    int ans = solution.lengthOfLongestSubstring(s);
    cout << ans << endl;
}