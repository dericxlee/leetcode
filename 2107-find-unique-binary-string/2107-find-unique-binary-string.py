class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binary = "01"
        nums_set = set(nums)

        def backtrack(array):
            if len(array) == len(nums):
                combo = "".join(array)

                if combo not in nums_set:
                    return combo
                return None
            
            for char in binary:
                array.append(char)
                result = backtrack(array)
                if result:
                    return result
                array.pop()
        
        return backtrack([])

