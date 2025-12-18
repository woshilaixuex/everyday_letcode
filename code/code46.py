from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        isHave = [False] * len(nums)
        def dfs(index: int):
            if(index >= len(nums)):
                ans.append(temp.copy())
                return
            for i in range(len(nums)):
                if (isHave[i] is False):
                    temp.append(nums[i])
                    isHave[i] = True
                    dfs(index+1)
                    temp.pop()
                    isHave[i] = False
            return 
        dfs(0)
        return ans
if __name__ == "__main__":
    list = [1,2,3]
    solutin = Solution()
    print(solutin.permute(list))