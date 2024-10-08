class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = len(nums)

        for i in range(len(nums)):
            counter += i - nums[i]
        
        return counter
        