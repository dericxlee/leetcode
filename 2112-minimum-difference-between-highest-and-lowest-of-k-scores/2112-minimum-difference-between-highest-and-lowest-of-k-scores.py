class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) < 2 or len(nums) < k:
            return 0

        nums.sort()
        ans = nums[k - 1] - nums[0]

        for i in range(1, len(nums) - k + 1):
            diff = nums[i+k-1] - nums[i]

            ans = min(ans, diff)
        
        return ans

