from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binSeach():
            left = 0
            right = len(nums) - 1
            while(left < right):
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return nums[left]
        return binSeach()
if __name__ == "__main__":
    solution = Solution()
    nums = [11,13,15,17]
    print(solution.findMin(nums))