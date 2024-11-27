class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        result = []
        
        def bfs(graph):
            queue = deque([0])
            count = 0
            seen = set([0])

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    if node == n - 1:
                        return count
                
                    queue.append(node + 1)

                    for road in graph[node]:
                        if road not in seen:
                            seen.add(road)
                            queue.append(road)
                
                count += 1
        
        for u, v in queries:
            graph[u].append(v)
            result.append(bfs(graph))

        return result
        




        

        
        
