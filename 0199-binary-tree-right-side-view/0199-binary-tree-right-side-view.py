# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if not node:
                return
            
            if level == len(res):
                res.append(node.val)
            
            dfs(node.right, 1 + level)
            dfs(node.left, 1 + level)
        
        dfs(root, 0)
        return res