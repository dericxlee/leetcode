class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, sum(candies) // k

        while left <= right:
            mid = (left + right) // 2

            if sum(candy // mid for candy in candies) >= k:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

        

