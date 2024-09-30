class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = list(string.ascii_lowercase + string.ascii_uppercase + "0123456789")

        left = 0
        right = len(s) - 1

        while left < right:   
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            elif s[left] not in letters:
                left += 1
            elif s[right] not in letters:
                right -= 1
            else:
                return False
        
        return True

