class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        courses_needed = [0] * (numCourses)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            courses_needed[course] += 1

        queue = deque([i for i in range(numCourses) if courses_needed[i] == 0])
        taken = set()
        
        while queue:
            node = queue.popleft()
            taken.add(node)

            for course in graph[node]:
                courses_needed[course] -= 1

                if courses_needed[course] == 0:
                    queue.append(course)
        
        return len(taken) == numCourses