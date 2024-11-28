class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[float('inf')]*col for _ in range(row)]
        dp[0][0] = 0
        queue = deque([(0, 0)])
        seen = set([(0, 0)])

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < row and 0 <= dy < col and (dx, dy) not in seen:
                    seen.add((dx, dy))
                    dp[dx][dy] = min(dp[dx][dy], dp[x][y] + grid[dx][dy])

                    if not grid[dx][dy]:
                        queue.appendleft((dx, dy))
                    else:
                        queue.append((dx, dy))

        return dp[-1][-1]









            
