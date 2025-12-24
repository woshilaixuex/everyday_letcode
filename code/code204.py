from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.ans = -1
        def dfs(root:Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            self.index += 1
            if self.index == k:
                self.ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.ans
if __name__ == "__main__":
    solution = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.left.right = TreeNode(2)
    tree.right = TreeNode(4)
    print(solution.kthSmallest(tree,1))