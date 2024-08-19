class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        vowels = list('aeiouAEIOU')
        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] not in vowels:
                left+=1
            elif arr[right] not in vowels:
                right-=1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1

        return ''.join(arr)

