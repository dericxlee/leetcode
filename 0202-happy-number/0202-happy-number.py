class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        while n != 1 and n not in nums:
            nums.add(n)
            sum = 0

            for digits in str(n):
                sum += int(digits)**2
            
            n = sum
        
        return n == 1
        