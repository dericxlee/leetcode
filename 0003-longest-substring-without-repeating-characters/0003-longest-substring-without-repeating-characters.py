class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        freq = defaultdict(int)
        l, result = 0, 0

        for r in range(len(s)):
            char = s[r]
            freq[char] += 1

            while freq[char] > 1:
                tail = s[l]
                freq[tail] -= 1
                l += 1
            
            result = max(result, r - l  + 1)

        return result