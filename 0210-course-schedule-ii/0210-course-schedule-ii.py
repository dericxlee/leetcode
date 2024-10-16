class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        courses = [0] * (numCourses)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            courses[course] += 1

        queue = deque([i for i in range(numCourses) if courses[i] == 0])
        res = []
        taken = 0

        while queue:
            node = queue.popleft()
            res.append(node)
            taken += 1

            for course in graph[node]:
                courses[course] -= 1

                if courses[course] == 0:
                    queue.append(course)
        
        return res if taken == numCourses else []

