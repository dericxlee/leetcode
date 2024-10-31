# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = [0]
        idx = 0

        dummy = ListNode()
        curr = dummy

        fast1 = l1
        fast2 = l2

        while fast2 and fast1:
            fast1 = fast1.next
            fast2 = fast2.next

        node1 = l1
        node2 = l2
        
        while fast1:
            res.append(node1.val)
            fast1 = fast1.next
            node1 = node1.next
            idx += 1

        while fast2:
            res.append(node2.val)
            fast2 = fast2.next
            node2 = node2.next
            idx += 1
        
        while node1 and node2:
            sum = node1.val + node2.val
            carry = sum // 10
            remain = sum % 10
            i = idx

            while carry and i >= 0:
                print(i)
                carry_sum = carry + res[i]
                print(carry_sum)
                carry = carry_sum // 10
                carry_remain = carry_sum % 10

                res[i] = carry_remain
                i-=1

            idx+=1
            res.append(remain)

            node1 = node1.next
            node2 = node2.next
        
        if not res[0]:
            res.pop(0)

        for num in res:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next


        
