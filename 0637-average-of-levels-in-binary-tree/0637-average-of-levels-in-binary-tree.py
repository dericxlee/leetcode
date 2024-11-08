# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []

        while queue:
            dividend = 0
            divisor = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                dividend += node.val
                divisor += 1
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(dividend/divisor)
        
        return result
