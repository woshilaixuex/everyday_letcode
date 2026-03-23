#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> temp;
        int n = nums.size();
        dfs(nums,0,ans,temp);
        return ans;
    }
    void dfs(vector<int>& nums,int start,vector<vector<int>>&  ans,vector<int>& temp) {
        ans.push_back(temp);
        for (auto i = start;i < nums.size();i++) {
            temp.push_back(nums[i]);
            dfs(nums,i+1,ans,temp);
            temp.pop_back();
        }
    }
};
int main() {
    Solution solution;
    vector<int> nums = {1,2,3};
    vector<vector<int>> ans =  solution.subsets(nums);
}