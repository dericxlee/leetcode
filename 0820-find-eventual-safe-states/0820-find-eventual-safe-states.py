class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        edges = [0]*len(graph)
        queue = deque()
        result = []

        for i in range(len(graph)):
            if not graph[i]:
                queue.append(i)
                result.append(i)

            for edge in graph[i]:
                path[edge].append(i)
                edges[i] += 1
        
        while queue:
            node = queue.popleft()

            for neighbor in path[node]:
                edges[neighbor] -= 1
                
                if edges[neighbor] == 0:
                    result.append(neighbor)
                    queue.append(neighbor)
        
        result.sort()
        return result



        




    