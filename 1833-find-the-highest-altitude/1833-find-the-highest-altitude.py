class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        current = 0

        for height in gain:
            current += height
            result = max(result, current)

        return result