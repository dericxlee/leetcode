class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i]*=2
                nums[i+1] = 0
            
        l, r = 0, 1

        while r < n:
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] == 0:
                r += 1
                continue
            
            l += 1
            r += 1
        
        return nums
        

