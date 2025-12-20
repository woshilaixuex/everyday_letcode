from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        dummy = ListNode()
        curr = dummy
        while True:
            minVal = float('inf')
            minIndex = -1

            for i, node in enumerate(lists):
                if node and node.val < minVal:
                    minVal = node.val
                    minIndex = i

            if minIndex == -1:
                break
            node = lists[minIndex]
            lists[minIndex] =  node.next
            node.next = None
            curr.next = node
            curr = curr.next
        return dummy.next