class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        words.append(words[0])

        for i in range(n):
            first = words[i]
            next = words[i+1]

            if first[-1] != next[0]:
                return False
        
        return True
            

