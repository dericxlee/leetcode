import random

class Solution:

    def __init__(self, nums: List[int]):
        self.idx = {}
        for i in range(len(nums)):
            if nums[i] not in self.idx:
                self.idx[nums[i]] = []
            
            self.idx[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.idx[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)