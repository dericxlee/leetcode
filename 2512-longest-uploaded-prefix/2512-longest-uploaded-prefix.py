class LUPrefix:

    def __init__(self, n: int):
        self.min_heap = []
        self.max_heap = []

    def upload(self, video: int) -> None:
        if video == len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -video)
        else:
            heapq.heappush(self.min_heap, video)

        while self.min_heap and self.min_heap[0] == len(self.max_heap) + 1:
            video = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, - video)
        

    def longest(self) -> int:
        if self.max_heap:
            return abs(self.max_heap[0])
        
        return 0


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()