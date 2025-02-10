class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        visited = set([0])

        while queue:
            n = queue.popleft()

            if n not in visited:
                for room in rooms[n]:
                    queue.append(room)
                
                visited.add(n)
        
        return len(rooms) == len(visited)