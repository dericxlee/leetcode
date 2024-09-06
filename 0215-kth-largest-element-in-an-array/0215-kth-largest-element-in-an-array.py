import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)

        for num in nums[k:]:
            heapq.heappush(h, num)
            heapq.heappop(h)
        
        return heapq.heappop(h)