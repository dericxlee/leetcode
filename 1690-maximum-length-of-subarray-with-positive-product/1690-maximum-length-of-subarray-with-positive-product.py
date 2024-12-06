class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, result = 0, 0, 0

        for num in nums:
            if num > 0:
                pos += 1
                neg += 1 if neg > 0 else 0
            elif num < 0:
                neg += 1 if neg > 0 else 0
                pos += 1
                neg, pos = pos, neg
            else:
                pos, neg = 0, 0

            result = max(pos, result)

        return result
