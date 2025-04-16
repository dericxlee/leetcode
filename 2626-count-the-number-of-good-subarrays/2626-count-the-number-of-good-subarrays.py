class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        pairs = 0
        result = 0
        l = 0

        for r in range(n):
            num = nums[r]
            freq[num] += 1
            pairs += freq[num] - 1
            
            while pairs >= k:
                result += n - r
                tail = nums[l]
                pairs -= freq[tail] - 1
                freq[tail] -= 1
                l += 1
        
        return result







