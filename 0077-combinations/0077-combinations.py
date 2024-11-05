class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, k, array):
            if not k:
                result.append(array.copy())
                return
            
            for i in range(start, n-k+2):
                array.append(i)
                backtrack(i+1, k-1, array)
                array.pop()
        
        backtrack(1, k, list())
        return result
            

