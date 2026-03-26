#include<bits/stdc++.h>

using namespace std;

// 字节考察左右2分
int binSeachL(vector<int>& nums,int tag) {
    int left = 0,right = nums.size()-1;
    int ans = nums.size();
    while (left <= right) {
        int mid = (left + right) / 2;
        if (nums[mid] >= tag) {
            ans = mid;
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }
    return ans;
}
int binSeachR(vector<int>& nums,int tag) {
    int left = 0,right = nums.size() - 1;
    int ans = -1;
    while (left <= right) {
        // int mid = left + (right - left) / 2
        int mid = (right + left) / 2;
        if (nums[mid] <= tag) {
            ans = mid;
            left = mid + 1;
        }else {
            right = mid - 1;
        }
    }
    return ans;
}
int main() {
    vector<int> nums = {1,2,3,4,4,5,6,6,7};
    int left = binSeachL(nums,7);
    int right = binSeachR(nums,7);
    cout << left <<  " " << right << endl;
}