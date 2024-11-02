class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        if row*col != r*c:
            return mat
        
        queue = deque([num for row in mat for num in row])
        new_mat = [[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                new_mat[i][j] = queue.popleft()
        
        return new_mat


