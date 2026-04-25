#include<bits/stdc++.h>
using namespace std;
// 快排模板（基于中值）
void binQuickSort(int left,int right,vector<int>& nums) {
    if (left >= right) return;
    int l = left,r = right;
    int mid = left + ((right - left) >> 1);
    int temp = nums[mid];
    swap(nums[mid],nums[left]);
    while(l < r) {
        while(r > l&&nums[r] >= temp) r--;
        while(l < r&&nums[l] <= temp) l++;
        if(l < r) swap(nums[r],nums[l]);
    }
    swap(nums[l],nums[left]);
    binQuickSort(left,l-1,nums);
    binQuickSort(l+1,right,nums);
}
// 优化递归深度快排

// 三路快排
void thQuickSort(){

}
int main() {
    vector<int> nums = {5,4,3,2,4};
    binQuickSort(0,nums.size()-1,nums);
    for (auto i = 0;i < nums.size();i++) {
        cout << nums[i] << endl;
    }
}