from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node:Optional[TreeNode],pre_max=float("+inf"),pre_min=float("-inf"))->bool:
            if not node:
                return True
            if node.val <= pre_min or node.val >= pre_max:
                return False
            return check(node.left,node.val,pre_min) and check(node.right,pre_max,node.val)
        return check(root)
