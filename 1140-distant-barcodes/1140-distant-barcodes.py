class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        wait = deque()
        heap = []
        res = []

        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))

        while heap:
            freq, num = heapq.heappop(heap)
            res.append(num)

            if wait:
                heapq.heappush(heap, wait.popleft())

            if freq + 1 < 0:
                wait.append((freq+1,num))

        return res