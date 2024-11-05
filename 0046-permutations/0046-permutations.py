class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()

        def backtrack(array):
            if len(array) == len(nums):
                result.append(array.copy())
                return
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    array.append(num)
                    backtrack(array)
                    array.pop()
                    seen.remove(num)
        
        backtrack(list())
        return result
