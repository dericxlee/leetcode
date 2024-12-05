class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        current = 1

        for num in nums:
            if num < current:
                continue

            if num > current:
                return current
            
            current += 1
        
        return current
            
            