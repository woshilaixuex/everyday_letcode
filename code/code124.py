from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxAns = float("-inf")
        def maxSum(node:Optional[TreeNode]) -> int:
            if not node:
                return 0
            mSum = node.val
            leftSum = max(maxSum(node.left),0)
            rightSum = max(maxSum(node.right),0)
            sum = mSum + leftSum + rightSum
            self.maxAns = max(sum,self.maxAns)
            # 提供贡献只能选其一，不然做不到一条路径
            return sum + max(leftSum,rightSum)
        maxSum(root)
        return self.maxAns