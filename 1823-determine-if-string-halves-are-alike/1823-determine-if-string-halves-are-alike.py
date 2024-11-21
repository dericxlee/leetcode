class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = int(len(s) / 2)
        s1 = s[:n]
        s2 = s[n:]
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        counter = 0
        
        for i in range(n):
            if s1[i] in vowels:
                counter += 1
            
            if s2[i] in vowels:
                counter -= 1
        
        return counter == 0