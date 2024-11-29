class TrieNode():
    def __init__(self):
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def _insert(self, word):
        n = len(word)
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.children and i < n - 1:
                return 0
            
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            
            node = node.children[word[i]]
        
        return i + 1

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        length = 0
        result = ""

        for word in words:
            output = trie._insert(word)
            if output > length:
                result = word
                length = output
        
        return result
    



