from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        heap = [] 
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else :
                hashMap[num] = 1
        for num, count in hashMap.items():
            if len(heap) == k:
                if heap[0][0] < count:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(count,num))
            else :
                heapq.heappush(heap,(count,num))
        return [num for _, num in heap]
if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    ans = solution.topKFrequent(nums,k)
    print(ans)