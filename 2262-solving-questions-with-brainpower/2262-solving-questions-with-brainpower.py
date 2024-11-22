class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]*len(questions)
        dp[-1] = questions[-1][0]

        for i in range(len(questions)-2, -1, -1):
            score = questions[i][0]
            pointer = questions[i][1]

            if i + pointer < len(questions) - 1:
                score += dp[i + pointer + 1]
            
            dp[i] = max(dp[i+1], score)
        
        return dp[0]
