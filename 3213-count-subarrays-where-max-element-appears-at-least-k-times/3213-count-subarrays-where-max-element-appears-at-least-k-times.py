class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        mx = max(nums)
        n = len(nums)
        mx_count = 0
        ans = 0

        for right in range(n):
            if nums[right] == mx:
                mx_count +=1
            
            while mx_count == k:
                ans += n - right
                if nums[left] == mx:
                    mx_count-=1
                left+=1
            
        return ans

