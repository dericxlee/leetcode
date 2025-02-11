class SmallestInfiniteSet:

    def __init__(self):
        self.infinite = set([i for i in range(1, 1001)])
        self.heap = list([i for i in range(1, 1001)])
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        num = heapq.heappop(self.heap)
        self.infinite.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.infinite:
            heapq.heappush(self.heap, num)
            self.infinite.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)