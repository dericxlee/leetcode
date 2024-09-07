class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            num = abs(heapq.heappop(heap))
            heapq.heappush(heap, -math.floor(math.sqrt(num)))
        
        return abs(sum(heap))
