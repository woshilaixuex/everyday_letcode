#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int len = nums.size();
        quickSort(nums,0,len-1);
        return nums;
    }
    void quickSort(vector<int>& nums,int left,int right){
        if (left >= right) {
            return;
        }
        int mid = left + right >> 1;
        int pivot = nums[mid];
        int l = left,r = right;
        while(l <= r) {
            while(nums[r] > pivot) r--;
            while(nums[l] < pivot) l++;
            if (l <= r) {
                swap(nums[l],nums[r]);
                r--;
                l++;
            }
        }
        quickSort(nums,left,r);
        quickSort(nums,l,right);
    }
    void quickSort1(vector<int>& nums,int left,int right){
        if (left >= right) {
            return;
        }
        int pivot = nums[left];
        int l = left,r = right;
        while(l < r) {
            while(l < r&&nums[r] >= pivot) r--;
            while(l < r&&nums[l] <= pivot) l++;
            swap(nums[l],nums[r]);
        }
        swap(nums[l],nums[left]);
        quickSort(nums,left,l-1);
        quickSort(nums,l+1,right);
    }
};