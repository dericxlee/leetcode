class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref_sum = {0: 1}
        ans = 0
        odd_count = 0

        for num in nums:
            odd_count += num % 2

            if odd_count - k in pref_sum:
                ans += pref_sum[odd_count - k]
            
            pref_sum[odd_count] = pref_sum.get(odd_count, 0) + 1
        
        return ans
