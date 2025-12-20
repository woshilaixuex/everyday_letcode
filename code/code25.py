from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while True:
            end = prev
            for _ in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            start = prev.next
            next_group = end.next
            end.next = None
            group = self.reverse(start)
            prev.next = group
            start.next = next_group
            prev = start

    def reverse(self, head)->ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev