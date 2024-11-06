class Solution:
    def countArrangement(self, n: int) -> int:
        result = 0

        def backtrack(index, seen):
            nonlocal result

            if len(seen) == n:
                result+=1
                return
            
            for i in range(1, n+1):
                if i in seen or (i % index != 0 and index % i != 0):
                    continue
                
                seen.add(i)
                backtrack(index+1, seen)
                seen.remove(i)
        
        backtrack(1, set())
        return result
                

            
