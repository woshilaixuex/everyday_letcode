#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size(),i = n-2;
        if (n <= 1) {
            return;
        }
        while (i >= 0&&nums[i] >= nums[i+1]) {
            i--;
        }
        if (i > 0) {
            int j = n-1;
            while (nums[i] >= nums[j]) {
                j--;
            }
            swap(nums[i],nums[j]);
        }
        reverse(nums.begin()+i+1,nums.end());
    }
};