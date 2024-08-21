class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        product = 1
        n = len(nums)

        for right in range(n):
            product*= nums[right]
            while product >= k and left <= right:
                product//= nums[left]
                left+=1
            
            count += right - left + 1

        return count
