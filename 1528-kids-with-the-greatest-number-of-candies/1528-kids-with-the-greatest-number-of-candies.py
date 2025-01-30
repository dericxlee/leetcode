class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False]*n
        minCandies = max(candies) - extraCandies
        
        for i in range(n):
            if candies[i] >= minCandies:
                result[i] = True

        return result
        