class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre = [0]*(N+1)
        suff = [0]*(N+1)
        for x in range(N):
            if nums[x] == 0:
                pre[x+1] = pre[x] + 1
            else:
                pre[x+1] = pre[x]
        for x in range(N-1,-1,-1):
            if nums[x] == 1:
                suff[x] = suff[x+1]+1
            else:
                suff[x] = suff[x+1]
        ans = []
        mx = 0
        for x in range(N+1):
            if suff[x]+pre[x] > mx:
                ans = [x]
                mx= suff[x]+pre[x]
            elif suff[x]+pre[x]==mx:
                ans.append(x)
        return ans 