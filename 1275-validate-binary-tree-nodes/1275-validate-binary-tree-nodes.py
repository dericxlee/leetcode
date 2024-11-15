class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        head = set([i for i in range(n)])
        graph = defaultdict(list)

        for i in range(n):
            if leftChild[i] >= 0 and leftChild[i] not in head:
                return False
            if leftChild[i] >= 0:
                head.remove(leftChild[i])
                graph[i].append(leftChild[i])

            if rightChild[i] >= 0 and rightChild[i] not in head:
                return False
            if rightChild[i] >= 0:
                head.remove(rightChild[i])
                graph[i].append(rightChild[i])
        
        if len(head) != 1: return False

        pathed = set()

        def dfs(node):
            if node in pathed:
                return False
            
            pathed.add(node)

            for child in graph[node]:
                dfs(child)
        
        dfs(head.pop())

        return len(pathed) == n





