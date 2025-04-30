class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            digits = 1
            while num >= 10:
                num //= 10
                digits += 1

            if digits % 2 == 0:
                result += 1

        return result