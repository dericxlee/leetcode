class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        n = len(nums)
        ans = 0

        for i in range(k, n+1):
            div = int(nums[i-k: i])
            if div != 0 and num % div == 0:
                ans+=1
        
        return ans