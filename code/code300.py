from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] * n
        maxNum = -1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i],arr[j]+1)
                    maxNum = max(arr[i],maxNum)
        return maxNum
if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,6,7,9,4,10,5,6]
    print(solution.lengthOfLIS(nums))