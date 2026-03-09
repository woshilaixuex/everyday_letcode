from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ans.append(index+1)
            else:
                nums[index] = -nums[index]
        return ans
if __name__ == "__main__":
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    ans = solution.findDuplicates(nums)
    print(ans)