class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        match = {index: char for index, char in enumerate(secret)}
        freq = Counter(secret)

        for idx, char in enumerate(guess):
            if match[idx] == char:
                bulls+=1
                if freq[char]:
                    freq[char] -=1
                else:
                    cows-=1
            elif char in freq and freq[char]:
                freq[char] -=1
                cows+=1

        return str(bulls) + 'A' + str(cows) + 'B'


