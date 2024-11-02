class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque()

        for i in range(row):
            for j in range(col):
                if not mat[i][j]:
                    queue.append((i, j))
                else:
                    mat[i][j] = 10000
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            i, j = queue.popleft()

            for di, dj in directions:
                pi, pj = i + di, j + dj
                if 0 <= pi < row and 0 <= pj < col and mat[pi][pj] > mat[i][j] + 1:
                    mat[pi][pj] = mat[i][j] + 1
                    queue.append((pi, pj))

        return mat
                    
