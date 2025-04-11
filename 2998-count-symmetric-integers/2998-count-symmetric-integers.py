class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        for i in range(low, high + 1):
            nums = list(str(i))
            n = len(nums)

            if n % 2 == 1:
                continue
            
            if sum(int(nums[i]) for i in range(n//2)) == sum(int(nums[i]) for i in range(n//2, n)):
                result += 1
        
        return result
        
