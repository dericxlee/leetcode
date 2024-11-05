class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r'[^\w]+', paragraph)
        freq = defaultdict(int)
        banned_words = set(banned)
        result = ''

        for word in words:
            word = word.lower()

            if word in banned_words:
                continue

            freq[word] += 1

            if freq[word] > freq[result]:
                result = word
        
        return result
            