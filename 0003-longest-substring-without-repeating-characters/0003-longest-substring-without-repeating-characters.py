class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        idx = 0
        ans = idx
        lookup = {}

        for i in range(len(s)):
            if s[i] in lookup and lookup[s[i]] >= idx:
                idx = lookup[s[i]] + 1

            lookup[s[i]] = i

            ans = max(ans, i - idx + 1)
        
        return ans





