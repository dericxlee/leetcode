class TrieNode():
    def __init__(self):
        self.children = {}
        self.final = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()

        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]

            curr.final = True
        
        array = sentence.split(' ')

        for i, word in enumerate(array):
            curr = root
            pref = ''
            for char in word:
                if char not in curr.children:
                    break
                
                pref += char
                curr = curr.children[char]

                if curr.final:
                    array[i] = pref
                    break

                

        return ' '.join(array)

