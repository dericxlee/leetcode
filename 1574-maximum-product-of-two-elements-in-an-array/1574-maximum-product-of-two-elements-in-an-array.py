class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        res = 1

        for num in nums:
            heapq.heappush(heap, num-1)
        
            if len(heap) > 2:
                heapq.heappop(heap)
            
        for _ in range(len(heap)):
            res*=heapq.heappop(heap)
        
        return res