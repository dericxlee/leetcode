class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0

        for num in nums:
            curr = num
            streak = 1

            while curr**2 in num_set:
                streak += 1
                curr = curr**2
            
            max_streak = max(max_streak, streak)
            
        return max_streak if max_streak > 1 else -1
            

