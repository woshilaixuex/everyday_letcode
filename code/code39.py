from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        def dfs(start: int,tgt:int):
            if tgt == 0:
                ans.append(arr.copy())
                return
            if tgt < 0:
                return
            for index,candidate in enumerate(candidates):
                if index < start:
                    continue
                arr.append(candidate)
                dfs(index,tgt - candidate)
                arr.pop()
            return
        dfs(0,target)
        return ans
if __name__ == "__main__":
    candidates = [2,3,6,7]
    solution = Solution()
    ans = solution.combinationSum(candidates,7)
    print(ans)