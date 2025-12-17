from typing import List
class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
            利用二进制遍历
            000 001 010 011 100 以此遍历
            时间复杂度：n*(2^n-1)
            空间复杂度：n -> temp辅助
        """
        ans = []
        temp = []
        m = 2 ** len(nums)
        for mark in range(m): 
            temp.clear()
            for i in range(len(nums)):
                if mark >> i & 1:
                    temp.append(nums[i])
            ans.append(temp.copy())
        return ans
    def subsets2(self,nums: List[int]) -> List[List[int]]:
        """
            利用回溯
            从0开始往length推 分为选中与未选的状态
            时间复杂度：n*(2^n-1)
            空间复杂度：n -> temp辅助
        """
        ans = []
        temp = []
        def dfs(cur:int):
            if cur == len(nums):
                ans.append(temp.copy())
                return 
            temp.append(nums[cur])
            dfs(cur+1)
            temp.pop(nums[cur])
            dfs(cur+1)
        dfs(0)
        return ans
if __name__ == "__main__":
    nums = [1,2,3]

