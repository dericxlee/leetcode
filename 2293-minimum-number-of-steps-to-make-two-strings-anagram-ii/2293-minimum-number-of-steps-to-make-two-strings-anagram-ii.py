class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0]*26
        result = 0

        for char in s:
            freq[ord(char)-ord('a')] += 1
        
        for char in t:
            freq[ord(char)-ord('a')] -= 1
        
        for i in range(26):
            result += abs(freq[i])
        
        return result

