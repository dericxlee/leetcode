class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        gcell = set(tuple(guard) for guard in guards)
        wcell = set(tuple(wall) for wall in walls)
        guarded = set()

        def dfs(i, j, di, dj):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in gcell or (i, j) in wcell:
                return
            
            guarded.add((i, j))
            dfs(i+di, j+dj, di, dj)

        for x, y in guards:
            dfs(x+1, y, 1, 0)
            dfs(x-1, y, -1, 0)
            dfs(x, y+1, 0, 1)
            dfs(x, y-1, 0, -1)
    
        return m*n - len(guarded) - len(gcell) - len(wcell)
