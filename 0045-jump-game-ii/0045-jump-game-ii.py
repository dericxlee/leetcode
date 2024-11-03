class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))

        for i in range(len(nums)):
            step = nums[i]
            for j in range(1, step+1):
                if i+j < len(nums) and dp[i+j] == 0:
                    dp[i+j] = dp[i] + 1
        
        return dp[-1]