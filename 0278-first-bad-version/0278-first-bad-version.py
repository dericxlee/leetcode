# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0

        while start <= n:
            mid = (start + n) // 2

            if isBadVersion(mid):
                n = mid - 1
            else:
                start = mid + 1
        
        return start