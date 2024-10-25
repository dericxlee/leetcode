class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1]*n
        nums = nums*2

        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                if idx < n:
                    res[idx] = nums[i]
            
            stack.append(i)
        
        return res
                

