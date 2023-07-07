"""
implemented heap cuz thats easier to save the minimum distance along with the points
run time beats 61.1%
memory beats 60.59
"""
from heapq import *
class Solution:
    def kClosest(self, points, k):
        cd = []
        size = len(points)
        closest = []
        for i in range(size):
            heappush(cd,(points[i][0] ** 2 + points[i][1] ** 2, points[i]))
        for i in range(k):
            closest.append(heappop(cd)[1])
        return closest


trial = Solution()
print(trial.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
