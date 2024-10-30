class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
            
        res = []
        left = 0
        right = 0

        while right < len(nums) - 1:
            if nums[right+1] - nums[right] != 1:
                n1, n2 = nums[left], nums[right]
                res.append(str(n1) + "->" + str(n2)) if n1 != n2 else res.append(str(n1))
                right += 1
                left = right
            else:
                right +=1
        
        n1, n2 = nums[left], nums[right]
        res.append(str(n1) + "->" + str(n2)) if n1 != n2 else res.append(str(n1))
        
        return res
            



