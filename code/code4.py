from typing import List
import sys
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        确保nums1长度一定是最小的
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        lTotal = (len(nums1) + len(nums2) + 1) // 2
        left = 0
        right = len(nums1)
        while (left < right):
            i = (left + right) // 2
            j = lTotal - i
            if i < len(nums1) and nums1[i] < nums2[j-1]:
                left = i + 1
            else:
                right = i
        i = left
        j = lTotal - left
        nums1l =  -sys.maxsize if i <= 0 else nums1[i-1]
        nums1r = sys.maxsize if i >= len(nums1) else nums1[i]
        nums2l = -sys.maxsize if j <= 0 else nums2[j-1]
        nums2r = sys.maxsize if j >= len(nums2) else nums2[j]
        if ((len(nums1) + len(nums2)) % 2 == 0):
            ans = ( max(nums1l,nums2l) + min(nums1r,nums2r) ) / 2
        else:
            ans = max(nums1l,nums2l)
        return ans
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,3]
    nums2 = [2]
    ans = solution.findMedianSortedArrays(nums1,nums2)
    print(ans)