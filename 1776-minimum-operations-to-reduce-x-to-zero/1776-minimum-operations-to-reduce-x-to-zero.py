class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)

        left = length = current = 0

        for right in range(len(nums)):
            current += nums[right]
            
            while current > target:
                current -= nums[left]
                left += 1
            
            if current == target:
                length = max(length, right - left + 1)
        
        return len(nums) - length if length else -1
        
