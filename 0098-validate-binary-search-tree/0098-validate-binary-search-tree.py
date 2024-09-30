# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, floor, ceiling = queue.popleft()

            if not (floor < node.val < ceiling):
                return False
            
            if node.left:
                queue.append((node.left, floor, node.val))
            if node.right:
                queue.append((node.right, node.val, ceiling))
        
        return True
