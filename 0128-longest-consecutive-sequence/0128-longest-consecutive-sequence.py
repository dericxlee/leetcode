class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                current_num = num
                while current_num + 1 in nums_set:
                    count += 1
                    current_num += 1
                res = max(res, count)
        
        return res

