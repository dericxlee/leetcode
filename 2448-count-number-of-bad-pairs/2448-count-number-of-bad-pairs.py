class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)
        totalPairs = n*(n-1) // 2
        goodPairs = 0

        for i in range(n):
            diff = nums[i] - i

            goodPairs += freq[diff]
            freq[diff] += 1

        return totalPairs - goodPairs