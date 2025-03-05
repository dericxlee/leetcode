class Solution:
    def coloredCells(self, n: int) -> int:
        total = 1
        while n > 0:
            total += 4*(n-1)

            n -= 1
        
        return total