# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        result = 0
        
        while prev:
            result = max(result, head.val + prev.val)
            head = head.next
            prev = prev.next

        return result
        


