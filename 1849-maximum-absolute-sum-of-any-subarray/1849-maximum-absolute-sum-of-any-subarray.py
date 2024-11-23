class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp = [[0, 0]]*len(nums)
        dp[0] = [nums[0], nums[0]]
        result = abs(nums[0])

        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], nums[i] + dp[i-1][0])
            dp[i][1] = min(nums[i], nums[i] + dp[i-1][1])
            result = max(result, abs(dp[i][0]), abs(dp[i][1]))

        return result
