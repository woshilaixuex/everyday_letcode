from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        递归同步展开
        """
        if root:
            return
        self.curr = root
        def preorder(node:Optional[TreeNode]) :
            if node is None:
                return
            if node != self.curr:
                self.right = node
                self.left = None
            left = node.left
            right = node.right
            preorder(left)
            preorder(right)
        preorder(root)
        return
if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    solution = Solution()
    solution.flatten(tree)
    print()