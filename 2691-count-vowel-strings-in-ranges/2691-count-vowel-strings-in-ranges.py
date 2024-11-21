class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        dp = [0]*(len(words)+ 1)

        for i in range(len(words)):
            word = words[i]
            
            if word[0] in vowels and word[-1] in vowels:
                dp[i+1] = dp[i] + 1
            else:
                dp[i+1] = dp[i]
        
        result = [0]*len(queries)

        for i, (x, y) in enumerate(queries):
            result[i] = dp[y+1] - dp[x]
        
        return result




