#include<bits/stdc++.h>
using namespace std;
void quickSort(vector<int>& nums,int start,int end){
    if (start >= end) return;
    int temp = nums[start];
    int l = start,r = end;
    while(l < r) {
        while(l < r && nums[r] >= temp) r--;
        while(l < r && nums[l] <= temp) l++;
        if (l < r) swap(nums[l],nums[r]);
    }
    swap(nums[l],nums[start]);
    quickSort(nums,start,l-1);
    quickSort(nums,l+1,end);
}
int main(){
    vector<int> nums = {1,5,2,8,9};
    quickSort(nums,0,nums.size()-1);
    for (auto i = 0l;i < nums.size();i++) {
        cout << nums[i] << endl;
    }
}