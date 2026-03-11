from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # hash和快慢指针
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        curr = head
        while curr:
            if curr in hashSet:
                return True
            hashSet.add(curr)
            curr = curr.next
        return False