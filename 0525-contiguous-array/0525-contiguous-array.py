class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = { 0: -1 }
        ln = len(nums)
        count = 0
        ans = 0

        for i in range(ln):
            if nums[i] == 1:
                count+=1
            else:
                count-=1

            if count in prefix:
                ans = max(ans, i - prefix[count])
            else:
                prefix[count] = i
        return ans
