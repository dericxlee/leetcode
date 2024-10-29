# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.sum = ""

        def dfs(node):
            if not node:
                return
            
            self.sum += str(node.val)

            if not node.left and not node.right:
                self.res += int(self.sum)
            
            dfs(node.left)
            dfs(node.right)

            self.sum = self.sum[:-1]
        
        dfs(root)
        return self.res