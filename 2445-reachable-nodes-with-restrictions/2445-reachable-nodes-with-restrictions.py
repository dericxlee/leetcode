class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(set)
        visited = set()

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        def dfs(node):
            visited.add(node)

            for child in graph[node]:
                if child not in restricted and child not in visited:
                    dfs(child)
        
        dfs(0)
        return len(visited)



