# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr = [[], []]

        def dfs(node, i):
            if not node.left and not node.right:
                arr[i].append(node.val)
                return

            if node.left:
                dfs(node.left, i)
            if node.right:
                dfs(node.right, i)

        dfs(root1, 0)
        dfs(root2, 1)

        return arr[0] == arr[1]
        
