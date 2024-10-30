class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 2:
            return n == 1
        
        n = n / 2

        return self.isPowerOfTwo(n)