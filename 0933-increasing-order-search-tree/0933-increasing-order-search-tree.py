# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        current = dummy

        def dfs(node):
            nonlocal current
            if not node:
                return
            
            dfs(node.left)
            
            node.left = None
            current.right = node
            current = node

            dfs(node.right)
        
        dfs(root)
        return dummy.right
