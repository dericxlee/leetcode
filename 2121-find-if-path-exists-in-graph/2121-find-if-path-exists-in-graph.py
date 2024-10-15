class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(list)

        for a, b in edges:
            paths[a].append(b)
            paths[b].append(a)
        
        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbor in paths[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            
        return False
