class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        result = -1
        switch = [-1]*n
        dp = [0]*n

        def backtrack(node, time):
            nonlocal result
            if switch[node] == 1:
                return
            
            if switch[node] == 0:
                cycle = time - dp[node]
                result = max(result, cycle)
                return

            switch[node] = 0
            dp[node] = time
            next_node = edges[node]
            if next_node != -1:
                backtrack(next_node, time + 1)
            switch[node] = 1
        
        for i in range(n):
            if switch[i] == -1:
                backtrack(i, 1)
        
        return result
