class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(set)
        visited = set()

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        def dfs(node):
            if not graph[node]:
                return
            
            visited.add(node)

            for child in graph[node]:
                if child in restricted or child in visited:
                    continue
                dfs(child)
        
        dfs(0)
        return len(visited)



