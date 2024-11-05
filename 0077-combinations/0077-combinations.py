class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, k, array):
            if not k:
                result.append(array)
                return
            
            for i in range(start, n+1):
                backtrack(i+1, k-1, array+[i])
        
        backtrack(1, k, list())
        return result
            

