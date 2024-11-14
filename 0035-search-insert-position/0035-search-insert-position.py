class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def solve(start, end):
            if start > end:
                return end + 1
            
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return solve(start, mid - 1)
            
            if nums[mid] < target:
                return solve(mid + 1, end)
        
        return solve(0, len(nums) - 1)