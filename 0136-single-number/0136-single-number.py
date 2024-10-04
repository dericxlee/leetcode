class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                del counter[num]
        
        return next(iter(counter))