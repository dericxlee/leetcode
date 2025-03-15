class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float("inf")

        for n in range(l, r + 1):
            total = sum(nums[:n])
            if total > 0:
                result = min(result, total)
            
            for i in range(n, len(nums)):
                total += nums[i] - nums[i-n]
                if total > 0:
                    result = min(result, total)
            
        return result if result != float("inf") else -1
            








