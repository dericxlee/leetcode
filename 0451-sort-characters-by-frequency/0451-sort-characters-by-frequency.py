class Solution:
    def frequencySort(self, s: str) -> str:
        letters = Counter(s)
        heap = []
        res = ''

        for key, count in letters.items():
            heapq.heappush(heap, (-count, key))
        
        while heap:
            count, key = heapq.heappop(heap)
            res+=key*abs(count) 

        return res


