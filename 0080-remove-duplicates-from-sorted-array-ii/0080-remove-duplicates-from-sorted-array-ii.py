class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        ans = len(nums)-1

        while p1 <= ans-2:
            p2 = p1 + 1
            p3 = p1 + 2

            if nums[p1] != nums[p2] or nums[p2] != nums[p3]:
                p1+=1
            else:
                nums.remove(nums[p3])
                ans-=1
        
        return ans+1
