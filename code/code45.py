from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0
        end = 0
        step = 0
        while start < len(nums) - 1:
            i = start
            step += 1
            maxend = end
            while i <= end:
                if i + nums[i] > maxend:
                    start = i
                    maxend = i + nums[i]
                i += 1
            end = maxend
            if end >= len(nums) - 1:
                break
        return step
    def jump__(self, nums: List[int]) -> int:
        """
        题解优化版本
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.jump(nums))