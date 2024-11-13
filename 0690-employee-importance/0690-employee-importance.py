"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        lookup = defaultdict(int)

        for employee in employees:
            lookup[employee.id] = employee

        def dfs(num):
            count = lookup[num].importance

            if not lookup[num].subordinates:
                return count

            for sub in lookup[num].subordinates:
                count += dfs(sub)
            
            return count
        
        return dfs(id)