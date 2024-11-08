class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        row, col = len(grid), len(grid[0])

        for i in range(row):
            temp += grid[i]
        
        for _ in range(k):
            num = temp.pop()
            temp.insert(0, num)
        
        result = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                result[i][j] = temp.pop(0)
        
        return result
        