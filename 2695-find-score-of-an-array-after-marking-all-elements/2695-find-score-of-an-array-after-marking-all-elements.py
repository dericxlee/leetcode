class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        heap = []
        marked = set()

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        while heap:
            num, idx = heapq.heappop(heap)

            if idx not in marked:
                marked.update([idx - 1, idx, idx + 1])
                score += num
        
        return score
            
            

            


