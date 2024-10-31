class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        num_set = set()
        max_val = float("-inf")

        for num in nums:
            if num in num_set:
                continue

            heapq.heappush(heap, num)
            max_val = max(max_val, num)
            num_set.add(num)

            if len(heap) > 3:
                heapq.heappop(heap)
            
        return heapq.heappop(heap) if len(heap) == 3 else max_val

        

