class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0

        for i in nums:
            sum += i
            self.prefix.append(sum)
        
        print(self.prefix)
       


    def sumRange(self, left: int, right: int) -> int:
        rsum = self.prefix[right]
        lsum = self.prefix[left - 1] if left>0 else 0
        return rsum - lsum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)