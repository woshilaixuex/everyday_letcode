#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (auto i = 0;i < n;i++) {
            while (nums[i] > 0&&nums[i] < n&&nums[nums[i]-1] != nums[i]) {
                swap(nums[nums[i]-1],nums[i]);
            }
        }
        for (auto i = 0;i < n;i++) {
            if (nums[i] != i+1) {
                return i+1;
            }
        }
        return n+1;
    }
};
int main() {
    Solution solution;
    vector<int> nums = {1,1};
    int ans = solution.firstMissingPositive(nums);
    cout << ans << endl;
}