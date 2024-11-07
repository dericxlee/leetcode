class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.final = False

class Trie():
    
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.final = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        row, col = len(board), len(board[0])
        used = set()

        def backtrack(i, j, node, string):
            if node.final:
                result.append(string)
                node.final = False
            
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] not in node.children or (i, j) in used:
                return
            
            char = board[i][j]
            
            used.add((i, j))

            backtrack(i-1, j, node.children[char], string+char)
            backtrack(i+1, j, node.children[char], string+char)
            backtrack(i, j-1, node.children[char], string+char)
            backtrack(i, j+1, node.children[char], string+char)

            used.remove((i, j))

        trie = Trie()

        for word in words:
            trie._insert(word)
        
        for i in range(row):
            for j in range(col):
                backtrack(i, j, trie.root, '')

        return result
