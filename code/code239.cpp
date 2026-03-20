#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<pair<int,int>> queue; // key,val
        int n = nums.size();
        vector<int> ans;
        for (int i = 0;i < k;i++) {
            while (!queue.empty() && nums[i] > queue.back().second) {
                queue.pop_back();
            }
            queue.push_back({i,nums[i]});
        }
        ans.push_back(queue.front().second);
        for (int i = k;i < n;i++) {
            while (!queue.empty() && nums[i] > queue.back().second) {
                queue.pop_back();
            }
            queue.push_back(pair(i,nums[i]));
            if (queue.front().first == i - k) {
                queue.pop_front();
            }
            ans.push_back(queue.front().second);
        }
        return ans;
    }
};