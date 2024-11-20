class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = Counter(s)

        if not k:
            return k

        if 'a' not in freq or 'b' not in freq or 'c' not in freq or freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1
        
        left = 0
        length = -1

        for right in range(len(s)):
            char = s[right]
            freq[char] -= 1

            while left <= right and freq[char] < k:
                freq[s[left]] += 1
                left += 1
            
            length = max(length, right - left + 1)
        
        return len(s) - length if length != -1 else -1
            



