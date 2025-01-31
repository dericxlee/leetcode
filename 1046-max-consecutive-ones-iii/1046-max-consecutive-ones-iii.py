class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        result = 0

        for r in range(len(nums)):
            if not nums[r]:
                k -= 1
            
            while k < 0:
                if not nums[l]:
                    k += 1
                
                l += 1

            result = max(result, r - l + 1)

        return result