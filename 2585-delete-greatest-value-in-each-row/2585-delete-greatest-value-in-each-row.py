class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)):
            grid[i] = [-n for n in grid[i]]
            heapq.heapify(grid[i])
        
        while grid[0]:
            max_val = []

            for i in range(len(grid)):
                max_val.append(-heapq.heappop(grid[i]))
            
            res += max(max_val)
        
        return res

