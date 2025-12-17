from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if root is None :
            return 0
        self.dfs(root)
        return self.ans - 1
    def dfs(self,root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        leftNum = self.dfs(root.left)
        rightNum = self.dfs(root.right)
        # left，right Num为节深度， + 1是根节点的父节点与其对应的边
        self.ans = max(self.ans,rightNum + leftNum + 1)
        # 返回节点深度
        return max(rightNum,leftNum) + 1
        
if __name__ == "__main__":
    """
    测试用例：
        1
       / \
      2   3
     / \
    4   5

    直径：4 -> 2 -> 1 -> 3 = 3 条边
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)


    sol = Solution()
    result = sol.diameterOfBinaryTree(root)
    print("二叉树直径 =", result)