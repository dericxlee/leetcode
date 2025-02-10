class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        queue = deque()

        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue.append(i)
                provinces += 1

                while queue:
                    city = queue.popleft()
                    
                    for j in range(n):
                        if isConnected[city][j] == 1 and j not in visited:
                            visited.add(j)
                            queue.append(j)

        return provinces






