from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.curr = 0
        if len(preorder) == 0:
            return None
        n = len(preorder)
        def createTree(left:int,right:int) -> Optional[TreeNode]:
            if left > right:
                return None
            root = TreeNode(preorder[self.curr])
            self.curr += 1
            index = 0
            for index in range(left,right+1):
                if inorder[index] == root.val:
                    break
            root.left = createTree(left,index-1)
            root.right = createTree(index+1,right)
            return root
        tree = createTree(0,n-1)
        return tree
    def buildTree_pro(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        用map记录下标
        '''
        self.curr = 0
        if not preorder:
            return None
        n = len(preorder)
        hash_map = {val:idx for idx,val in enumerate(inorder)}
        def createTree(left:int,right:int) -> Optional[TreeNode]:
            if left > right:
                return None
            root = TreeNode(preorder[self.curr])
            self.curr += 1
            index = hash_map[root.val]
            root.left = createTree(left,index-1)
            root.right = createTree(index+1,right)
            return root
        tree = createTree(0,n-1)
        return tree
if __name__ == "__main__":
    soultion = Solution()
    preorder = [1,2]
    inorder = [1,2]
    tree = soultion.buildTree(preorder,inorder)