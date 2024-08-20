class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1

        while even <= len(nums) - 2 and odd <= len(nums) - 1:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 != 0:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        
        return nums