class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        high = nums[0]
        low = nums[0]
        result = abs(nums[0])

        for i in range(1, len(nums)):
            high = max(nums[i] + high, nums[i])
            low = min(nums[i] + low, nums[i])
            result = max(result, abs(high), abs(low))
        
        return result