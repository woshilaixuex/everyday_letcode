from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lenght = 0
        n = len(nums)
        i = 0
        while i <= lenght:
            lenght = max(lenght,i + nums[i])
            if lenght >= n - 1:
                return True
            i += 1
        return False
if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.canJump(nums))