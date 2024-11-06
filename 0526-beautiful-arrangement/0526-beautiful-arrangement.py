class Solution:
    def countArrangement(self, n: int) -> int:
        seen = [False]*(n+1)

        def backtrack(index):
            if index > n:
                return 1

            count = 0

            for i in range(1, n+1):
                if seen[i]:
                    continue

                if i % index == 0 or index % i == 0:
                    seen[i] = True
                    count += backtrack(index+1)
                    seen[i] = False

            return count
        
        return backtrack(1)

