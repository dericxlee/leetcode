# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def dfs(node, level):
            if not node:
                return

            if len(self.res) < level + 1:
                self.res.append(node.val)
            
            if self.res[level] < node.val:
                self.res[level] = node.val
            
            dfs(node.left, 1 + level)
            dfs(node.right, 1 + level)
        
        dfs(root, 0)
        return self.res
            

            
