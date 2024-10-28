class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        map = {}
        res = 0
        
        for num in nums:
            if num in map:
                map[num**2] = map[num] + 1
            else:
                map[num**2] = 1
            
            res = max(res, map[num**2])
        
        if res < 2:
            return -1
        
        return res
         