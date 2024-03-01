class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        sh = 1
        points.sort()
        rt = points[0]
        for x in range(1, N):
            if points[x][0] <= rt[1]:
                rt[0] = max(rt[0], points[x][0])
                rt[1] = min(rt[1], points[x][1])
            else:
                rt = points[x]
                sh += 1
        return sh
