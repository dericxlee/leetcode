class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        seen = [False]*(len(nums))

        def backtrack(array):
            if len(array) == len(nums):
                result.append(array.copy())
                return
            
            for i in range(len(nums)):
                if seen[i] or (i > 0 and nums[i] == nums[i-1] and not seen[i-1]):
                    continue

                seen[i] = True
                array.append(nums[i])
                backtrack(array)
                array.pop()
                seen[i] = False

        backtrack(list())
        return result
