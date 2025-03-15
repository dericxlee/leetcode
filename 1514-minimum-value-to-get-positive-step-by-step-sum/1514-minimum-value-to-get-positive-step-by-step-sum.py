class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        floor = 0
        total = 0

        for num in nums:
            total += num
            floor = min(floor, total)

        return abs(floor) + 1