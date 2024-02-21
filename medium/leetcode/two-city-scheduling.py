class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = sorted(costs, key = lambda x:x[0]-x[1])
        b = sorted(costs, key = lambda x:x[1]-x[0])
        N = len(costs)
        s = 0
        for i in range(N//2):
            s += a[i][0]
            s += a[N-i-1][1]
        r = 0
        for j in range(N//2):
            r += b[j][1]
            r += b[N-j-1][0]
        return min(r,s)