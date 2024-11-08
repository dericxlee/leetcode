class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        r, c = len(matrix), len(matrix[0])

        row = defaultdict(int)
        col = defaultdict(int)

        for i in range(r):
            row[i] = min(matrix[i])

        for i in range(r):
            for j in range(c):
                col[j] = max(col[j], matrix[i][j])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == row[i] and matrix[i][j] == col[j]:
                    result.append(matrix[i][j])

        return result