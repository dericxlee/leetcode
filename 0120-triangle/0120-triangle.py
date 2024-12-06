class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[sys.maxsize]*(n+1) for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1]) if i > 0 else triangle[i][j] + dp[i-1][j]

        return min(dp[-1])


