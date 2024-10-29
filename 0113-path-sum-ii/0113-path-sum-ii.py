# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(node, sum):
            if not node:
                return

            subset.append(node.val)
            sum-=node.val
            
            if not node.left and not node.right and sum == 0:
                res.append(subset.copy())

            dfs(node.left, sum)
            dfs(node.right, sum)

            subset.pop()
        
        dfs(root, targetSum)
        return res

