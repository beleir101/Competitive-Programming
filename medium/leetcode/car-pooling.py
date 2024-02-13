class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx, mn = 0,float('inf')

        for x in trips:
            mx = max(mx, x[2])
            mn = min(mn, x[1])
        N = mx-mn +1
        pr = [0]*(N+2)
        for x in trips:
            pr[x[1]-mn+1] += x[0]
            pr[x[2]-mn+1] -= x[0]
        mv = 0
        for x in range(N):
            pr[x+1] += pr[x]
            mv = max(mv, pr[x])
        return mv <= capacity