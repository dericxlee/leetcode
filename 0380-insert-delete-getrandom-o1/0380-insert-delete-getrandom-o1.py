import random

class RandomizedSet:

    def __init__(self):
        self.nums = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        else:
            self.nums[val] = len(self.nums)
            self.num_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False

        idx = self.nums[val]
        last = self.num_list[-1]

        self.nums[last] = idx
        self.num_list[idx] = last

        del self.nums[val]
        self.num_list.pop()
        return True

    def getRandom(self) -> int:
        if self.num_list:
            return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()