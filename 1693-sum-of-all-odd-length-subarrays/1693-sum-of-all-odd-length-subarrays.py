class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
            
        prefix = [0]*len(arr)
        prefix[0] = arr[0]

        for i in range(len(arr)):
            prefix[i] = prefix[i-1] + arr[i]
        
        result = 0

        for i in range(1, len(arr)+1, 2):
            total = prefix[i - 1]
            result += total

            for j in range(i, len(arr)):
                total = prefix[j] - prefix[j- i]
                result += total

        return result