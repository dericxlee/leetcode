class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        
        if n < 3:
            return n == 1

        return self.isPowerOfThree(n/3)