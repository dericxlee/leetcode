class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        res = []
        
        for word, freq in count.items():
            heapq.heappush(heap, [-freq, word])
        
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            res.append(word)

        return res

