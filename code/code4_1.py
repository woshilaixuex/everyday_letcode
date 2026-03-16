from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 < nums2:
            nums1,nums2 = nums2,nums1
        n1,n2 = len(nums1),len(nums2)
        