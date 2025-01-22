class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])

        visited = set()
        counter = 0
        queue = deque([])

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited.update([(i, j)])
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                print((x, y))
                isWater[x][y] = counter

                for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited:
                        queue.append((dx, dy))
                        visited.update([(dx, dy)])
        
            counter += 1
        
        return isWater

                    


        
        