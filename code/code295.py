import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = [] # 较大部分
        self.maxHeap = [] # 较小部分
        
    def addNum(self, num: int) -> None:
        if len(self.minHeap) != len(self.maxHeap):
            heapq.heappush(self.minHeap,num)
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.maxHeap,-num)
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
    def findMedian(self) -> float:
        return self.minHeap[0] if len(self.minHeap) != len(self.maxHeap) else (-self.maxHeap[0] + self.minHeap[0]) / 2.0
            
if __name__ == "__main__":
    median = MedianFinder()
    median.addNum(1)
    median.addNum(2)
    print(median.findMedian())
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()