class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([tuple(entrance)])
        result = 0
        visited = set([tuple(entrance)])
        n, m = len(maze), len(maze[0])

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if (x == 0 or y == 0 or x == n - 1 or y == m - 1) and result:
                    return result
                
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= dx < n and 0 <= dy < m and maze[dx][dy] == "." and (dx, dy) not in visited:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            
            result += 1

        return -1
                

