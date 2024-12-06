class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
            
        n = len(triangle)
        dp = [[sys.maxsize]*(n) for _ in range(n)]
        dp[0][0] = triangle[0][0]
        result = sys.maxsize

        for i in range(1, n):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])

                if i == n - 1:
                    result = min(result, dp[i][j])

        return result


