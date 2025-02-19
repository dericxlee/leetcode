class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        result = set()

        def backtrack(array, visited):
            if array:
                result.add("".join(array))
                
            if len(visited) == n:
                return
            
            for i in range(n):
                if i not in visited:
                    array.append(tiles[i])
                    visited.add(i)
                    backtrack(array, visited)
                    array.pop()
                    visited.remove(i)
    
        backtrack(list(), set())
        return len(result)