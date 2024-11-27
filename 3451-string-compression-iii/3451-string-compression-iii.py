class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        letter = word[0]
        count = 1

        for i in range(1, len(word)):
            if word[i] != letter or count == 9:
                comp += str(count) + letter
                letter = word[i]
                count = 1
            else:
                count += 1
        
        return comp + str(count) + letter

