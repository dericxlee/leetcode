class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [0]*(rowIndex+1)
        dp[0] = 1

        for n in range(rowIndex):
            for i in range(rowIndex, 0, -1):
                dp[i] += dp[i-1]
        
        return dp