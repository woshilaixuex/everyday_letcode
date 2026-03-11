from typing import List,Optional
from queue import PriorityQueue
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dump = ListNode(-1)
        temp = dump
        priQueue = PriorityQueue()
        for i, list in enumerate(lists):
            if list:
                priQueue.put((list.val,i,list))
        while not priQueue.empty():
            _,i,node = priQueue.get()
            temp.next = node
            temp = temp.next
            node = node.next
            if node:
                priQueue.put((node.val,i,node))
        return dump.next
if __name__ == "__main__":
    lists = [ListNode(1,ListNode(4,ListNode(5))),
             ListNode(1,ListNode(3,ListNode(4))),
             ListNode(2,ListNode(6))]
    solution = Solution()
    ans = solution.mergeKLists(lists)
    print(ans)