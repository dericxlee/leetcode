class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        trie = Trie()

        for i in range(n):
            node = trie.root

            for j in range(n):
                num = grid[i][j]
                if num not in node.children:
                    node.children[num] = TrieNode()
                node = node.children[num]
            
            node.count += 1
        
        for j in range(n):
            node = trie.root

            for i in range(n):
                num = grid[i][j]
                if num not in node.children:
                    continue
                node = node.children[num]
            
            result += node.count
        
        return result
        

        

                    