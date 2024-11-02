class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0: continue

                perimeter += 4

                if i > 0 and grid[i-1][j] == 1: perimeter -= 1
                if j > 0 and grid[i][j-1] == 1: perimeter -= 1
                if i < row - 1 and grid[i+1][j] == 1: perimeter -= 1
                if j < col - 1 and grid[i][j+1] == 1: perimeter -= 1

        return perimeter