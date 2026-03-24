#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        if (n <= 0) return {-1,-1};
        int l = 0,r = n-1;
        int left = binSeach(nums,target-1);
        int right = binSeach(nums,target) - 1;
        if (left >= n||nums[left] != target) {
            return {-1,-1};
        }
        return {left,right};        
    }
    int binSeach(vector<int>& nums,int target) {
        int n = nums.size();
        int l = 0,r = n-1;
        while (l <= r) {
            int mid = l + r >> 1;
            if (nums[mid] > target) {
                r = mid - 1;
            }else {
                l = mid + 1;
            }
        }
        return l;
    }
};
int main() {
    Solution solution;
    vector<int> nums = {5,7,7,8,8,10};
    vector<int> ans = solution.searchRange(nums,8);
    cout << ans[0] <<" "<<  ans[1] << endl;
}