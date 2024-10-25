class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = True

        for i in range(len(nums) - 1):
            if nums[i] - nums[i+1] > 0:
                increase = False
            
            if nums[i] - nums[i+1] < 0:
                decrease = False
        
        return increase or decrease
