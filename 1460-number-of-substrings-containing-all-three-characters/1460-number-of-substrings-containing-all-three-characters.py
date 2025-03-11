class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        seen = set()

        l, result = 0, 0
        n = len(s)

        for r in range(n):
            char = s[r]
            freq[char] += 1
            seen.add(char)

            while len(seen) == 3:
                result += n - r

                tail = s[l]
                freq[tail] -= 1
                
                if freq[tail] == 0:
                    seen.remove(tail)
                
                l += 1
            
        return result

