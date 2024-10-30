# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.path = []

        def dfs(node):
            if not node:
                return
            
            self.path.append(str(node.val))

            if not node.left and not node.right:
                string = "->".join(self.path)
                self.res.append(string)
            
            dfs(node.left)
            dfs(node.right)
            self.path.pop()
        
        dfs(root)
        return self.res