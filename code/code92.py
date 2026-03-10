from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween0(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def rever(head:Optional[ListNode]):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

        dump_head = ListNode(-1)
        dump_head.next = head
        prev_node = dump_head

        for _ in range(left-1):
            prev_node = prev_node.next
        curr = prev_node
        for _ in range(right - left + 1):
            curr = curr.next
        end_node = curr.next
        left_node = prev_node.next
        right_node = curr

        curr.next = None
        rever(left_node)
        prev_node.next = right_node
        left_node.next = end_node

        return dump_head.next
    # 1. prev -> curr -> next -> end
    # 2. prev -> curr -> end <- next
    # 3. prev -> curr -> end;next -> curr
    # 4. prev -> next -> curr -> end
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dump_node = ListNode(-1)
        dump_node.next = head
        prev = dump_node
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        for _ in range(right - left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
        return dump_node.next
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    ans = solution.reverseBetween(head,2,4)
    print(ans)