class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        seen = [False]*(len(nums)+1)

        def backtrack(array):
            if len(array) == len(nums):
                result.append(array.copy())
                return
            
            num_set = set()
            
            for i in range(len(nums)):
                if seen[i] or nums[i] in num_set:
                    continue
                
                num_set.add(nums[i])

                seen[i] = True
                array.append(nums[i])
                backtrack(array)
                array.pop()
                seen[i] = False

        backtrack(list())
        return result
