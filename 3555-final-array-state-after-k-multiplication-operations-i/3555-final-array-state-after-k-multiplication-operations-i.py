class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_value = min(nums)
            index = nums.index(min_value)
            nums[index] *= multiplier
        
        return nums