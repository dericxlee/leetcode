# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.freq = defaultdict(int)
        self.res = []

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            curr_sum = node.val + left + right
            self.freq[curr_sum] += 1
            return curr_sum

        dfs(root)

        most_freq = 0
        
        for value in self.freq.values():
            most_freq = max(most_freq, value)
        
        for key in self.freq.keys():
            if self.freq[key] == most_freq:
                self.res.append(key)
        
        return self.res


