class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(sum, i):
            if (sum, i) in memo:
                return memo[(sum, i)]

            if i >= len(nums) and sum == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            result = dfs(sum+nums[i], i+1) + dfs(sum-nums[i], i+1)
            memo[(sum, i)] = result
            return result
        
        return dfs(0, 0)