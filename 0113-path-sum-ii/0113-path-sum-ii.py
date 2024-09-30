# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return root

        queue = deque([(root, root.val, [root.val])])
        res = []

        while queue:
            node, sum, path = queue.popleft()

            if not node.left and not node.right and sum == targetSum:
                res.append(path)

            if node.left:
                queue.append((node.left, sum+node.left.val, path+[node.left.val]))
            if node.right:
                queue.append((node.right, sum+node.right.val, path+[node.right.val]))
        
        return res