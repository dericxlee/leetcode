# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        res = head
        carry = 0

        while l1 and l2:
            head.next = ListNode()
            head = head.next
            sum = l1.val + l2.val + carry
            carry = sum // 10

            head.val = sum % 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            head.next = ListNode()
            head = head.next
            sum = l1.val + carry
            carry = sum // 10

            head.val = sum % 10
            l1 = l1.next
        
        while l2:
            head.next = ListNode()
            head = head.next
            sum = l2.val + carry
            carry = sum // 10

            head.val = sum % 10
            l2 = l2.next
        
        if carry != 0:
            head.next = ListNode()
            head.next.val = carry
        
        return res.next
        
        

            
