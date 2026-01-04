from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        l:找到第一个大于等于target的
        r:找到第一个大于target
        """
        if not nums:
            return [-1,-1]
        def binSeach(target: int) -> int:
            l = 0
            r = len(nums) # 这里故意右移一位
            while (l < r):
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else :
                    r = mid
            return l
        left = binSeach(target)
        right = binSeach(target+1) - 1
        if left == len(nums) or nums[left] != target: #做特判不等于len,即tgt不大于所有数
            return [-1, -1]
        return [left,right]
if __name__ ==  "__main__":
    solution = Solution()
    nums = [1,2,3]
    target = 4
    print(solution.searchRange(nums,target))