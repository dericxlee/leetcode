class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}
        mapped = set()

        for i in range(len(s)):
            if s[i] in map and map[s[i]] != t[i]:
                return False
            
            if t[i] in mapped and s[i] not in map:
                return False
            
            map[s[i]] = t[i]
            mapped.add(t[i])
        
        return True

            
            