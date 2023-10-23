"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import defaultdict
class Solution:
    def __init__(self):
        self.tt = 0
    def getImportance(self, employees, id):
        p = defaultdict(list)
        for j in employees:
            p[j.id].append(j.importance)
            p[j.id].append(j.subordinates)
        visit = set()
        self.dfs(visit,p,id)
        return self.tt
    def dfs(self,visited,edges,element):
        if element in visited:
            return
        visited.add(element)
        self.tt += edges[element][0]
        for i in edges[element][1]:
            self.dfs(visited,edges,i)
trial = Solution()
print(trial.getImportance(employees = [[1,2,[5]],[5,-3,[]]], id = 5))