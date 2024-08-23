class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        counter = {}
        ans = 0
        sum = 0

        for right in range(len(nums)):
            counter[nums[right]] = counter.get(nums[right], 0) + 1
            sum += nums[right]

            while counter[nums[right]] > 1 and left < right:
                counter[nums[left]] -=1
                sum -= nums[left]
                left+=1
        
            ans = max(ans, sum)
        
        return ans



