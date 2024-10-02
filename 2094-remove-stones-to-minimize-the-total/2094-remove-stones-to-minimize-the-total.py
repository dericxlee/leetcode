class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]

        heapq.heapify(heap)

        for _ in range(k):
            pile = heappop(heap)
            pile = floor(pile/2)
            heappush(heap, pile)
        
        return abs(sum(heap))

