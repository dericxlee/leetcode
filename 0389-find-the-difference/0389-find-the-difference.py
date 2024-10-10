class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = Counter(s)

        for char in t:
            if char not in freq:
                return char
            else:
                freq[char] -= 1
            
            if freq[char] == 0:
                del freq[char]
        