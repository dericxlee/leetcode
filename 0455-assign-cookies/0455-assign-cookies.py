class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0

        i = len(g) - 1
        j = len(s) - 1

        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                count += 1
                i-=1
                j-=1
            else:
                i-=1
        
        return count

