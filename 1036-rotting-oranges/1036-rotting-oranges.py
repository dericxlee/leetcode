class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        visited = set()
        m, n = len(grid), len(grid[0])
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue and fresh:
            for _ in range(len(queue)):
                x, y = queue.popleft()
            
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited and grid[dx][dy] == 1:
                        fresh -= 1
                        queue.append((dx, dy))
                        visited.add((dx, dy))
                
            minutes += 1
        
        return minutes if not fresh else -1



        

    

