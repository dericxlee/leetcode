class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.zero = -1

    def add(self, num: int) -> None:
        if num:
            self.prefix.append(self.prefix[-1]*num)
        else:
            self.prefix = [1]
            self.zero = len(self.prefix) - 1
        

    def getProduct(self, k: int) -> int:
        n = len(self.prefix)

        if k >= len(self.prefix):
            return 0
        else:
            return self.prefix[n-1] // self.prefix[n-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)