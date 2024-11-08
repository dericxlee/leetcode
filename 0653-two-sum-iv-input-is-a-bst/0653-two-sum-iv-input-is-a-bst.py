# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        prefix = set()

        def dfs(node):
            if not node:
                return
            
            if node.val in prefix:
                return True
            
            prefix.add(k - node.val)
            
            if dfs(node.left) or dfs(node.right):
                return True
            
            return False
        
        return dfs(root)