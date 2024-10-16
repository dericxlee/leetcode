class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        graph = {i: [] for i in range(row)}
        visited = set()
        provinces = 0

        for n in range(row):
            for m in range(row):
                if isConnected[n][m]:
                    graph[n].append(m)

        for i in range(row):
            if i not in visited:
                provinces += 1
                queue = deque([i])

                while queue:
                    node = queue.popleft()
                    visited.add(node)

                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)

        return provinces
                     
                    




