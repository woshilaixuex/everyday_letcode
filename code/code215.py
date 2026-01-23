from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def buildHeap(heapSize):
            for i in range(heapSize//2-1,-1,-1):
                maxHeap(i,heapSize)
        def maxHeap(i,heapSize):
            l = i*2 + 1
            r = i*2 + 2
            largest = i
            if l < heapSize and nums[l] > nums[largest]:
                largest = l
            if r < heapSize and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                swap(largest,i)
                maxHeap(largest,heapSize)
        def swap(a,b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        heapSize = n
        buildHeap(heapSize)
        for i in range(n-1,n-k,-1):
            swap(0,i)
            heapSize -= 1
            maxHeap(0,heapSize)
        return nums[0]
if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    ans = solution.findKthLargest(nums,k)
    print(ans)