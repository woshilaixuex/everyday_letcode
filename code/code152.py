from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpMin = [0] * (n + 1)
        dpMax = [0] * (n + 1)
        ans = dpMax[1] = dpMin[1] = nums[0]
        for i,num in enumerate(nums):
            if i == 0:
                continue
            dpMax[i+1] = max(dpMin[i]*num,max(dpMax[i]*num,num))
            dpMin[i+1] = min(dpMax[i]*num,min(dpMin[i]*num,num))
            ans = max(dpMax[i+1],ans)
        return ans
if __name__ == "__main__":
    solution = Solution()
    nums = [5,6,-3,4,-3]
    ans = solution.maxProduct(nums)
    print(ans)