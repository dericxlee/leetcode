class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.zero = -1
        self.index = 1

    def add(self, num: int) -> None:
        if num:
            self.prefix.append(self.prefix[-1]*num)
        else:
            self.prefix.append(1)
            self.zero = self.index

        self.index += 1
        

    def getProduct(self, k: int) -> int:
        if self.index - k <= self.zero:
            return 0
        else:
            return self.prefix[self.index - 1] // self.prefix[self.index- k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)