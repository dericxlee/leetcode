# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        queue = deque([(root, 1)])

        while queue:
            node, type = queue.popleft()

            if not node.left and not node.right and type == 0:
                res += node.val
            
            if node.left:
                queue.append((node.left, 0))
            if node.right:
                queue.append((node.right, 2))
        
        return res

