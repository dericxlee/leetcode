class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        dp = [0]*(len(nums))

        for i in range(2, len(nums)):
            diff1 = nums[i] - nums[i-1]
            diff2 = nums[i-1] - nums[i-2]

            if diff1 == diff2:
                dp[i] += dp[i-1] + 1
                result += dp[i]
        
        return result
        


