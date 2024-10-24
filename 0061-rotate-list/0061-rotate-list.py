# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        end = head
        length = 1

        while end.next:
            end = end.next
            length += 1
        
        k = k % length
        end.next = head

        for _ in range(length - k):
            end = end.next
        
        new_head = end.next
        end.next = None

        return new_head




    
        
        

        


        