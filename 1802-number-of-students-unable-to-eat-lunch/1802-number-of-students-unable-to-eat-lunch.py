class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        rejected = 0

        while n > rejected:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                rejected = 0
                n -= 1
            else:
                students.append(students.pop(0))
                rejected +=1
        
        return n
            
            
