from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        stack = []
        ans = []
        stack.append(root)
        step = 1
        while stack:
            tempNode = []
            temp = []
            lenght = len(stack)
            if step % 2 != 0:
                for i in range(lenght):
                    temp.append(stack[i].val)
            else :
                for i in range(lenght-1,-1,-1):
                    temp.append(stack[i].val)
            for node in stack:
                if node.left is not None:
                    tempNode.append(node.left)
                if node.right is not None:
                    tempNode.append(node.right)
            step += 1
            stack = tempNode
            ans.append(temp)
        return ans
if __name__ == "__main__":
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    solution = Solution()
    ans = solution.zigzagLevelOrder(root)
    print(ans)