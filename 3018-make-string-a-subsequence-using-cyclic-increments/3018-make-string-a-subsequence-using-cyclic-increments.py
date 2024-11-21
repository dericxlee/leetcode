class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        left = right = 0
        print(ord('z'), ord('a'))

        while left < m and right < n:
            s1 = str1[left]
            s2 = str2[right]

            if ord(s1) == ord(s2) or (ord(s1) - 96) % 26 == ord(s2) - 97:
                right+=1
            
            left+=1
        
        return right == n