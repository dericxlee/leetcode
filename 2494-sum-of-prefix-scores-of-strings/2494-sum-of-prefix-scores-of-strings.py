class TrieNode():

    def __init__(self):
        self.children = {}
        self.score = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for word in words:
            current = root

            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.score += 1
        
        res = []

        for word in words:
            total_score = 0
            current = root

            for char in word:
                current = current.children[char]
                total_score += current.score
            
            res.append(total_score)

        return res