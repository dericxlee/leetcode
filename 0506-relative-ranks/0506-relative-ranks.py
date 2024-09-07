class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))
        
        for rank in range(len(score)):
            score_value, idx = heapq.heappop(heap)

            if rank == 0:
                score[idx] = "Gold Medal"
            elif rank == 1:
                score[idx] = 'Silver Medal'
            elif rank == 2:
                score[idx] = 'Bronze Medal'
            else:
                score[idx] = str(rank + 1)
        
        return score
