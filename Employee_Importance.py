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
        self.imp=0

        def find(id):
            for i in employees:
                if i.id==id:
                    return i

        
        def dfs(emp):
            self.imp += emp.importance
            for sub in find(emp.id).subordinates:
                subO= find(sub)
                dfs(subO)
                
        for employee in employees:
            if employee.id == id:
                dfs(employee)
                return self.imp

        return self.imp
        
