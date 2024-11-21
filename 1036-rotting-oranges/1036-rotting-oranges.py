class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while queue and fresh:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

                for x, y in directions:
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        fresh -= 1
                        grid[x][y] = 2
                        queue.append((x, y))
        
        return time if not fresh else -1
                

            
                    

