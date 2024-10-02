class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteSet = {i for i in range(1, 2000)}
        self.heap = [i for i in range(1, 2000)]

    def popSmallest(self) -> int:
        num = heapq.heappop(self.heap)
        self.infiniteSet.remove(num)

        return num

    def addBack(self, num: int) -> None:
        if num not in self.infiniteSet:
            heapq.heappush(self.heap, num)
            self.infiniteSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)