# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        stack = [root]
        tail = 0

        while stack:
            node = stack.pop()

            if tail:
                tail.right = node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                node.left = None
            
            tail = node
            





        