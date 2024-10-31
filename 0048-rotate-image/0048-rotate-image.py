class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        map = {}

        # transpose matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                map[(i, j)] = matrix[i][j]

                if (j, i) not in map:
                    matrix[i][j] = matrix[j][i]
                else:
                    matrix[i][j] = map[(j, i)]

        # reverse matrix rows
        for row in matrix:
            row.reverse()

