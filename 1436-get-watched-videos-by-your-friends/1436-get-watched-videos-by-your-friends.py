class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        current_level = 0
        queue = deque([id])
        visited = set([id])

        while queue and current_level < level:
            current_level += 1
            for _ in range(len(queue)):
                i = queue.popleft()

                for friend in friends[i]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            
        videos = list()

        while queue:
            i = queue.popleft()

            for video in watchedVideos[i]:
                videos.append(video)
        
        freq = Counter(videos)
        heap = []
        
        for x, y in freq.items():
            heapq.heappush(heap, (y, x))

        result = list()

        while heap:
            y, x = heapq.heappop(heap)
            result.append(x)

        return result




