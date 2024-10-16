class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for src, target, time in times:
            graph[src].append((target, time))

        queue = [(0, k)]
        nodes = set()

        while queue:
            total_time, node = heapq.heappop(queue)

            nodes.add(node)

            if len(nodes) == n:
                return total_time

            for target, time in graph[node]:
                if target not in nodes:
                    new_time = total_time + time

                    heapq.heappush(queue, (new_time, target))

        return -1

