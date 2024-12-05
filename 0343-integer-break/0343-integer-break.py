class Solution:
    def integerBreak(self, n: int) -> int:
        result = 1

        if n <= 4:
            return 2**(n-2)
        
        while n > 4:
            n -= 3
            result *= 3
        
        return result*n