class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n

        if not trust:
            return -1

        trustee = [0] * (n+1)
        trusters = [0] * (n+1)

        for a, b in trust:
            trustee[b] += 1
            trusters[a] += 1
        
        for i in range(n+1):
            if trustee[i] == n - 1 and trusters[i] == 0:
                return i
        
        return -1
