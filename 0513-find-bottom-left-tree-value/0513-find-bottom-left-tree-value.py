# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = None
        self.level = -1

        def dfs(node, row):
            if not node:
                return

            if row > self.level:
                self.level = row
                self.res = node.val
            
            dfs(node.left, 1+row)
            dfs(node.right, 1+row)
    
        dfs(root, 0)
        return self.res