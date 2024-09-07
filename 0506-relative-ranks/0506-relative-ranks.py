class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        counter = 1

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))
        
        while heap:
            scores, idx = heapq.heappop(heap)

            if counter == 1:
                score[idx] = "Gold Medal"
            elif counter == 2:
                score[idx] = 'Silver Medal'
            elif counter == 3:
                score[idx] = 'Bronze Medal'
            else:
                score[idx] = str(counter)
            
            counter+=1
        
        return score


