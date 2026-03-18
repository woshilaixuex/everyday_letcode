#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string str;
        generate(ans,n,str,0,0);
        return ans;
    }
    void generate(vector<string> &ans,int n,string &str,int left,int right) {
        if (str.size() == n) {
            ans.push_back(str);
        }
        if (left < n) {
            str.push_back('(');
            generate(ans,n,str,left+1,right);
            str.pop_back();
        }
        if (left > right) {
            str.push_back(')');
            generate(ans,n,str,left,right+1);
            str.pop_back();
        }
    }
};