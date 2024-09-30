# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        if not root:
            return res
        
        queue = deque([(root, str(root.val))])

        while queue:
            node, string = queue.popleft()

            if not node.left and not node.right:
                res += int(string)

            if node.left:
                queue.append((node.left, string + str(node.left.val)))
            if node.right:
                queue.append((node.right, string + str(node.right.val)))
    
        return res
            
