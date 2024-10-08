class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numcheck = Counter(nums)

        for n in range(len(nums)+1):
            if n not in numcheck:
                return n
        