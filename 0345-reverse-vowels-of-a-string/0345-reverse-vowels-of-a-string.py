class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        l = 0
        r = len(arr) - 1
        vowels = 'AEIOUaeiou'

        while l < r:
            print(l, r)
            if arr[l] in vowels and arr[r] in vowels:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            
            if arr[l] not in vowels:
                l += 1
            
            if arr[r] not in vowels:
                r -= 1

        return ''.join(arr)

