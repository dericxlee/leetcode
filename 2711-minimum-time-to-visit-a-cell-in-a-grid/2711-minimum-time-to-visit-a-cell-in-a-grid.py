class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            time, x, y = heapq.heappop(heap)

            if (x, y) == (row - 1, col - 1):
                return time

            if (x, y) in visited:
                continue
            
            visited.add((x, y))

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < row and 0 <= dy < col and (dx, dy) not in visited:
                    new_time = max(0, grid[dx][dy] - time)

                    if new_time % 2 == 0:
                        new_time += 1

                    heapq.heappush(heap, (new_time + time, dx, dy))
