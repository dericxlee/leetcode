class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        idx = dict()
        l, result = 0, 0

        for r in range(len(s)):
            char = s[r]
            
            if char in idx and idx[char] >= l:
                l = idx[char] + 1

            idx[char] = r
            
            result = max(result, r - l + 1)

        return result