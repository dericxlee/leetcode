class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_counter = {}
        set_counter = set()

        for num in nums:
            if num not in dict_counter and num not in set_counter:
                dict_counter[num] = 1
                set_counter.add(num)
            elif num in dict_counter:
                del dict_counter[num]
        
        return next(iter(dict_counter))