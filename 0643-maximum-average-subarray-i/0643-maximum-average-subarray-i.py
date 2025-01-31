class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        result = total / k
        l = 0

        for r in range(k, len(nums)):
            total += nums[r] - nums[l]
            l += 1

            result = max(result, total/k)

        return result

