class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted = candidates.sort()
        results = []

        def backtrack(start, target, array):
            if target == 0:
                results.append(array)
                return

            seen = set()

            for i in range(start, len(candidates)):
                if candidates[i] > target or candidates[i] in seen:
                    continue
                
                seen.add(candidates[i])
                backtrack(i+1, target-candidates[i], array+[candidates[i]])
        
        backtrack(0, target, [])
        return results
            
