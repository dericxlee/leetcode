class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, array):
            if len(array) > 1:
                result.append(array.copy())

            seen = set()
            
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                
                if start > 0 and array[-1] > nums[i]:
                    continue
                
                array.append(nums[i])
                seen.add(nums[i])
                backtrack(i+1, array)
                array.pop()
        
        backtrack(0, list())
        return result