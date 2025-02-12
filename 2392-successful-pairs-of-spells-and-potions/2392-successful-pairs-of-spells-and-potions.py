class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m, n = len(spells), len(potions)
        pairs = [0]*m
        potions.sort()

        for i in range(m):
            target = (success + spells[i] - 1) // spells[i] 
            index = bisect.bisect_left(potions, target)
            pairs[i] = n - index

        return pairs


