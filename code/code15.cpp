#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        if (n <= 2) {
            return ans;
        }
        for (auto i = 0;i < n;i++) {
            if (i > 0 && nums[i-1] == nums[i]) {
                continue;
            }
            int t = n - 1;
            int tag = -nums[i];
            for (auto j = i+1;j < n;j++) {
                if (j > i + 1 && nums[j-1] == nums[j]) {
                    continue;
                }
                while (j < t&&nums[j] + nums[t] > tag) {
                    --t;
                }
                if (t == j) {
                    break;
                }
                if (nums[j] + nums[t] == tag) {
                    ans.push_back({nums[i],nums[j],nums[t]});
                }
            }
        }
        return ans;
    }
};