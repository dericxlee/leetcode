class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        cd = deque()
        time = 0

        while heap or cd:
            time+=1

            if heap:
                task = heapq.heappop(heap) + 1

                if task:
                    cd.append((time + n, task))

            if cd and cd[0][0] == time:
                t, freq = cd.popleft()
                heapq.heappush(heap, freq)
            
        return time





