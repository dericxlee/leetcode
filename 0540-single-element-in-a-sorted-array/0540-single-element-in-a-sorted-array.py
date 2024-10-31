class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = 1

        while right < len(nums) - 1:
            if nums[left] != nums[right]:
                return nums[left]
            
            left += 2
            right += 2
        
        return nums[-1]