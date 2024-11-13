# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1

        def dfs(node, sum):
            if not node:
                return 0
            
            sum += node.val
            count = prefix[sum - targetSum]
            prefix[sum] += 1

            count += dfs(node.left, sum)
            count += dfs(node.right, sum)

            prefix[sum] -= 1

            return count
        
        return dfs(root, 0)

