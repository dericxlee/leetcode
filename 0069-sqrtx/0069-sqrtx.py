class Solution:
    def mySqrt(self, x: int) -> int:
        def solve(start, end):
            if start > end:
                return end

            mid = (start + end) // 2

            if mid * mid == x:
                return mid
            
            if mid * mid > x :
                return solve(start, mid - 1)
            else:
                return solve(mid + 1, end)
        
        return solve(0, x)