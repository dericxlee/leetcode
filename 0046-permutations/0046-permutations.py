class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*(len(nums))
        result = []

        def backtrack(array):
            if len(array) == len(nums):
                result.append(array.copy())
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    array.append(nums[i])
                    backtrack(array)
                    array.pop()
                    used[i] = False
        
        backtrack([])
        return result