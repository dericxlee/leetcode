class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        result = 0
        incr, decr = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incr += 1
                decr = 1
            elif nums[i] < nums[i-1]:
                incr = 1
                decr += 1
            else:
                incr = 1
                decr = 1
            
            result = max(result, incr, decr)
        
        return result