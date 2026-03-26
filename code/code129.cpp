#include<bits/stdc++.h>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
    int sum = 0;
public:
    int sumNumbers(TreeNode* root) {
        vector<int> number;
        sumNumber(root,number);
        return sum;
    }
    void sumNumber(TreeNode* root,vector<int> number) {
        number.push_back(root->val);
        if (!root->left&&!root->right) {
            int x = 0;
            for (auto n:number) {
                x = x*10 + n;
            }
            sum += x;
            return;
        }
        if (root->left) {
            sumNumber(root->left,number);
        }
        if (root->right) {
            sumNumber(root->right,number);
        }
    }
};
int main() {
    Solution solution;
    TreeNode* root = new TreeNode(1,new TreeNode(2),new TreeNode(3));
    int ans = solution.sumNumbers(root);
    cout << ans << endl;
}