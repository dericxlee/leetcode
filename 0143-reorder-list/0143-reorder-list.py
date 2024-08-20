# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        arr = []
        
        while start:
            arr.append(start.val)
            start = start.next

        print(arr)

        left = 0
        right = len(arr) - 1
        even = True

        while head:
            if even == True:
                head.val = arr[left]
                left+=1
                head = head.next
                even = False
            else:
                head.val = arr[right]
                right-=1
                head = head.next
                even = True
        
        return head
        
        