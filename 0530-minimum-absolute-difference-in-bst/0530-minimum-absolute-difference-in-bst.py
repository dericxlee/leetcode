# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")

        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, floor, ceiling = queue.popleft()
            res = min(res, abs(node.val - floor), abs(node.val - ceiling))

            if node.left:
                queue.append((node.left, floor, node.val))
            if node.right:
                queue.append((node.right, node.val, ceiling))
                
        return res
        

            

