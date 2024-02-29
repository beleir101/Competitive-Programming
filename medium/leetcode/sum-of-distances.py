class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        N = len(nums)
        ans = [0]*(N)
        for x in range(N):
            d[nums[x]].append(x)
        for x in d:
            n = len(d[x])
            if n > 1:
                pre = [0]*(n+1)
                for t in range(n):
                    pre[t+1] = pre[t]+d[x][t]
                for y in range(n):
                    vs = pre[y]
                    sv = pre[n]-pre[y]
                    ans[d[x][y]] = abs(vs-(d[x][y]*y))+(sv-(d[x][y]*(n-y-1)))-d[x][y]
            else:
                ans[d[x][0]] = 0
        return ans

        