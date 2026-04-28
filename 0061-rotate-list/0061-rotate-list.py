# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tail = head
        length = 0

        while tail:
            tail = tail.next
            length += 1
        
        dummy = ListNode(0, head)
        slow = fast = head

        for _ in range(k % length):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        dummy.next = slow.next
        slow.next = None
    
        return dummy.next
