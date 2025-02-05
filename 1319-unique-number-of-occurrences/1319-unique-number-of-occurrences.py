class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        check = set()

        for value in freq.values():
            if value in check:
                return False

            check.add(value)
            
        return True