class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = []
        
        while nums:
            left = 0
            right = len(nums) - 1

            avg = (nums[left] + nums[right])/ 2
            ans.append(avg)
            nums.remove(nums[right])
            nums.remove(nums[left])
            
        return min(ans)    


            