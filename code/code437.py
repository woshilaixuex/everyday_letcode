from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            计算以root根的树下等于targetSum的个数
        """
        def rootSum(root:Optional[TreeNode],targetSum:int)->int:
            '''
                计算以root为根起始计算的等于targetSum的个数
            '''
            if root is None:
                return 0
            ret = 0
            if root.val == targetSum:
                ret += 1
            ret += rootSum(root.left,targetSum-root.val)
            ret += rootSum(root.right,targetSum-root.val)
            return ret
        if root is None:
            return 0
        ans = 0
        # 选root为根起始
        ans = rootSum(root,targetSum)
        # 不选root以left,right为根
        ans += self.pathSum(root.left,targetSum)
        ans += self.pathSum(root.right,targetSum)
        return ans
if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    solution = Solution()
    print(solution.pathSum(tree,3))