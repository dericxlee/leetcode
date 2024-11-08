class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        queue = deque([(rCenter, cCenter)])
        result = []
        seen = set([(rCenter, cCenter)])
        
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            x, y = queue.popleft()
            result.append([x, y])

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny))
            
        return result
