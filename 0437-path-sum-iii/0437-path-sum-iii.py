# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, total):
            if not node:
                return 0

            total += node.val
            result = prefix[total - targetSum]

            prefix[total] += 1
            result += dfs(node.left, total)
            result += dfs(node.right, total)
            prefix[total] -= 1

            return result
        
        return dfs(root, 0)
            

