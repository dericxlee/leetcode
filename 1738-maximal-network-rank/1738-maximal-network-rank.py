class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        adj = [[0] * n for _ in range(n)]

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            adj[a][b] = 1
            adj[b][a] = 1
        
        maximal = 0

        for i in range(n):
            for j in range(i + 1, n):
                maximal = max(maximal, degree[i] + degree[j] - adj[i][j])
        
        return maximal
        