class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = defaultdict(int)
        result = 0

        for row in matrix:
            freq[tuple(row)] += 1
            freq[tuple([1 - x for x in row])] += 1

            result = max(result, freq[tuple(row)])
        
        return result


