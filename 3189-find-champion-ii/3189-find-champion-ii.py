class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        dp = [0]*n

        for x, y in edges:
            dp[y] += 1
        
        champion = None

        for i in range(n):
            if dp[i] == 0 and champion != None:
                return -1
                
            if dp[i] == 0 and champion == None:
                champion = i
            
        return champion