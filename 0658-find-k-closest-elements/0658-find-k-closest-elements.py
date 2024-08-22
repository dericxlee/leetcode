class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        n = len(arr)

        if n < k:
            return []

        for right in range(k, len(arr)):
            if arr[right] - x >= x - arr[left]:
                return arr[left:right]
            else:
                left+=1
        
        return arr[n - k:]
    
