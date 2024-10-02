class LUPrefix:

    def __init__(self, n: int):
        self.min_heap = []
        self.longest_prefix = 0

    def upload(self, video: int) -> None:
        if video == self.longest_prefix + 1:
            self.longest_prefix = video
        else:
            heapq.heappush(self.min_heap, video)

        while self.min_heap and self.min_heap[0] == self.longest_prefix + 1:
            self.longest_prefix = heapq.heappop(self.min_heap)
        
    def longest(self) -> int:
        return self.longest_prefix


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()