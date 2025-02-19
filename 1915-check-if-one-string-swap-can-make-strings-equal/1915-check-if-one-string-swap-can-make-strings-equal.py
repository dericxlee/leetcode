class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        swaps = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps.append(i)
            
            if len(swaps) > 2:
                return False
            
        if len(swaps) < 2:
            return False
        
        i = swaps[0]
        j = swaps[1]

        return (s1[i] == s2[j] and s1[j] == s2[i])
