class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        visited = set()
        result = 0

        for num in nums:
            if num < k:
                return -1
            
            if num > k and num not in visited:
                visited.add(num)
                result += 1
        
        return result
