from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 
        self.ans = root.val
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            value = node.val
            temp = value
            if left > 0:
                temp += left
            if right > 0:
                temp += right
            self.ans = max(self.ans,temp)
            if left > 0 or right > 0:
                value += max(left,right)
            return value
        dfs(root)
        return self.ans
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1,TreeNode(2),TreeNode(3))
    ans = solution.maxPathSum(root)
    print(ans)