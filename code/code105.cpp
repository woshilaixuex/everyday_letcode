#include<bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
    int dx = 0;
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buideTreeWithInorder(preorder,inorder,0,preorder.size()-1);
    }
    TreeNode* buideTreeWithInorder(vector<int>& preorder, vector<int>& inorder
        ,int left,int right) {
        if (left == right) {
            return new TreeNode(preorder[dx++]);
        }
        if (left > right) {
            return nullptr;
        }
        int tNodeVal = preorder[dx++];
        TreeNode* tree = new TreeNode(tNodeVal);
        int index = left;
        for (int i = left;i <= right;i++) {
            if (inorder[i] == tNodeVal) {
                index = i;
                break;
            }
        }
        tree->left = buideTreeWithInorder(preorder,inorder,left,index-1);
        tree->right = buideTreeWithInorder(preorder,inorder,index+1,right);
        return tree;
    }
};
int main() {
    vector<int> preo = {3,9,20,15,7};
    vector<int> ino = {9,3,15,20,7};
    Solution solution;
    TreeNode* tree = solution.buildTree(preo,ino);
}