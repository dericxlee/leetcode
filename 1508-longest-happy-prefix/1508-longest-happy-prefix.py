class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        result = ""

        for i in range(n - 1):
            prefix = s[:i + 1]
            suffix = s[n-i-1:n]

            if prefix == suffix:
                result = prefix
        
        return result

