#include<bits/stdc++.h>
using namespace std;
class Solution {
    vector<vector<int>> ans;
public:
    void dfs(vector<int>& candidates,vector<int> temp,int sum,int target,int start) {
        if (sum > target) return;
        if (sum == target) {
            ans.push_back(temp);
        }
        for (auto i = start;i < candidates.size();i++) {
            temp.push_back(candidates[i]);
            dfs(candidates,temp,sum+candidates[i],target,i);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        dfs(candidates,temp,0,target,0);
        return ans;
    }
};