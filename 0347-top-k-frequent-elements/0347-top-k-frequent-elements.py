class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        
        return res
        