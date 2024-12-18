class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, array):
            result.append(array.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                array.append(nums[i])
                backtrack(i+1, array)
                array.pop()
            
        backtrack(0, list())
        return result