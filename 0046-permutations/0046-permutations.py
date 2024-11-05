class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(count, array):
            if not count:
                result.append(array.copy())
                return
            
            for num in nums:
                if num not in array:
                    array.append(num)
                    backtrack(count-1, array)
                    array.pop()
        
        backtrack(len(nums), list())
        return result
