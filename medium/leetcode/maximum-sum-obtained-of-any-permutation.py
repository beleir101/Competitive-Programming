class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        pre = [0]*(N+1)
        mod = (10**9)+7
        d = defaultdict(int)
        for x in requests:
            pre[x[0]] += 1
            pre[x[1]+1] -= 1
        for y in range(1,N):
            pre[y] = pre[y]+pre[y-1]
        give = []
        for x in range(N):
            give.append(pre[x])
        nums.sort(reverse=True)
        give.sort(reverse=True)
        ans = 0
        for y in range(N):
            ans += give[y]*nums[y]
        return ans%mod