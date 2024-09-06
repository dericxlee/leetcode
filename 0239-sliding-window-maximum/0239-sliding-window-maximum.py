class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        left, right = 0, 0

        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            
            queue.append(right)
            right+=1

            while right - left + 1 > k:
                res.append(nums[queue[0]])
                left+=1

            while queue and queue[0] < left:
                queue.popleft()
        
        return res





