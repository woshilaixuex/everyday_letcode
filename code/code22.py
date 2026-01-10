from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backReturn(S,left,right):
            if (len(S) == 2 * n):
                ans.append("".join(S))
            if (left < n):
                S.append("(")
                backReturn(S,left+1,right)
                S.pop()
            if (right < left):
                S.append(")")
                backReturn(S,left,right+1)
                S.pop()
        backReturn([],0,0)
        return ans