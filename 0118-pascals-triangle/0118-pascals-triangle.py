class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [0]*(numRows+1)
        dp[0] = 1

        result = [[1]]

        for row in range(1, numRows):
            for i in range(numRows, 0, -1):
                dp[i] += dp[i-1]
            result.append(dp[0:row+1])
        
        return result