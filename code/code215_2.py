from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heap = heapq.heapify(maxHeap)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(maxHeap)
        return -ans
if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    ans = solution.findKthLargest(nums,k)
    print(ans)