class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append(-v)
            graph[v].append(u)

        queue = deque([0])
        visited = set([0])
        result = 0

        while queue:
            n = queue.popleft()
            visited.add(n)

            for neighbor in graph[n]:
                if abs(neighbor) not in visited:
                    if neighbor < 0: result += 1

                    queue.append(abs(neighbor))

        return result
