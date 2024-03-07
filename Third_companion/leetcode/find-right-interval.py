class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        st = sorted(intervals)
        en = sorted(intervals,key= lambda x: x[1])
        N = len(intervals)
        for x in range(N):
            d[intervals[x][0]] = x
        j = 0
        ans = [-1]*N
        for x in en:
            while j < N and st[j][0]<x[1]:
                j += 1
            if j >= N:
                break
            ans[d[x[0]]]=d[st[j][0]]
        return ans

