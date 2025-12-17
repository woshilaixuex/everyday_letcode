from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True
        return self.isMir(root.left,root.right)
    def isMir(self,t1:Optional[TreeNode],t2:Optional[TreeNode]) -> bool :
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val :
            return False
        return self.isMir(t1.left,t2.right) and self.isMir(t1.right,t2.left)