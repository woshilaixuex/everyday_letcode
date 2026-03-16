from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dump = ListNode(-1000)
        dump.next = head
        curr = dump
        slow = None
        frist = None
        while curr.next.next:
            slow = curr.next
            frist = curr.next.next
            if slow.val == frist.val:
                temp = slow.val
                while slow and slow.val == temp:
                    curr.next = slow.next
                    slow = curr.next
            else:
                curr = curr.next
        return dump.next
if __name__ == "__main__":
    solution = Solution()
    # list = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4))))))
    list = ListNode(1,ListNode(1))
    ans = solution.deleteDuplicates(list)
    while ans:
        print(ans.val)
        ans = ans.next