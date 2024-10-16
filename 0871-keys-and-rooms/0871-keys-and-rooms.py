class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict()
        visited = set()
        n = len(rooms)

        for i in range(n):
            graph[i] = rooms[i]
        
        queue = deque([0])

        while queue:
            node = queue.popleft()
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return len(visited) == n
