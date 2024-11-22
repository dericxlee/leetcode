class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
            result = max(result, dp[i])
        
        return result