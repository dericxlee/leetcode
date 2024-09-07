class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = set(nums)

        if 0 in n:
            return len(n) - 1
        else:
            return len(n)



        


