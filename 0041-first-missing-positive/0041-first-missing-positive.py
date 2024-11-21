class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        checked = set()
        result = 1
        
        for num in nums:
            if num > 0:
                checked.add(num)
            
            while result in checked:
                result += 1
        
        return result