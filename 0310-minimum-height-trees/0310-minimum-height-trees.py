class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0]*n

        if n == 1:
            degree[0] = 1

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        queue = deque()
        nodes = n

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        while nodes > 2:
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes -= 1

                for neighbor in graph[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        
        return list(queue)
