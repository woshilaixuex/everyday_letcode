from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        hash_map = {}
        def rightSee(cen:int,root: Optional[TreeNode]):
            if root is None:
                return 
            if cen not in hash_map.keys():
                ans.append(root.val)
                hash_map[cen] = True
            rightSee(cen+1,root.right)
            rightSee(cen+1,root.left)            
        rightSee(0,root)
        return ans
if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    solution = Solution()
    ans = solution.rightSideView(tree)
    print(ans)