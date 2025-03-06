class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set([i for i in range(1, n*n + 1)])
        twice = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] in nums:
                    nums.remove(grid[i][j])
                else:
                    twice = grid[i][j]

        missing = list(nums)

        return [twice] + missing