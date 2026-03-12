from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMid(head:ListNode) -> ListNode:
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def rever(head:ListNode) -> ListNode:
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        def merge(l1:ListNode,l2:ListNode):
            while l1 and l2:
                temp_l1 = l1.next
                temp_l2 = l2.next
                l1.next = l2
                l1 = temp_l1
                l2.next = l1
                l2 = temp_l2
            return
        mid = findMid(head)
        l1 = head
        l2 = mid.next
        l1.next = None
        l2 = rever(l2)
        merge(l1,l2)
if __name__ == "__main__":
    solution = Solution()
    lists = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
    solution.reorderList(lists)