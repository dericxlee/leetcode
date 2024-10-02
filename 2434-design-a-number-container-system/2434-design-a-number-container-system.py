class NumberContainers:

    def __init__(self):
        self.indexes = {}
        self.containers = {}

    def change(self, index: int, number: int) -> None:
        self.indexes[index] = number
        
        if number not in self.containers:
            self.containers[number] = []

        heapq.heappush(self.containers[number], index)

    def find(self, number: int) -> int:
        if number not in self.containers:
            return -1

        while self.containers[number]:
            idx = self.containers[number][0]
            if self.indexes[idx] == number:
                return idx
            heapq.heappop(self.containers[number])
         
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)