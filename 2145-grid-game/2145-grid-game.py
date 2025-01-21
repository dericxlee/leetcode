class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        prefix_top = [0]*n
        prefix_top[0] = grid[0][0]
        
        prefix_bot = [0]*n
        prefix_bot[0] = grid[1][0]

        for i in range(1, n):
            prefix_top[i] = prefix_top[i-1] + grid[0][i]
            prefix_bot[i] = prefix_bot[i-1] + grid[1][i]
        
        result = sys.maxsize

        for i in range(n):
            top_sum = prefix_top[-1] - prefix_top[i]
            bot_sum = prefix_bot[i-1] if i > 0 else 0

            optimal_path = max(top_sum, bot_sum)
            result = min(result, optimal_path)
        
        return result


