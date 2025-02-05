class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        prev = 0

        for i in range(len(nums)):
            left += prev
            right -= nums[i]
            prev = nums[i]

            if left == right:
                return i
        
        return -1