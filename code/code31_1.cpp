#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int l = nums.size() - 2,r = nums.size()-1;
        while (l >= 0 && nums[l] >= nums[l+1]) l--;
        if (l >= 0) {
            while (r >= 0 && nums[l] >= nums[r]) r--;
            swap(nums[l],nums[r]);
        }
        reverse(nums.begin()+l+1,nums.end());
    }
};
int main(){
    Solution solution;
    vector<int> arr = {1,2,3};
    solution.nextPermutation(arr);
    for (auto i = 0;i < arr.size();i++) {
        cout << arr[i];
    }
    cout << endl;
}