class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        p = []
        N = len(nums)
        for x in range(2*N):
            while len(p) > 0 and nums[p[-1]] < nums[x%N]:
                n = p.pop()
                d[n] = x%N
            p.append(x%N)
        ans = []
        for x in range(N):
            if x not in d:
                ans.append(-1)
            else:
                ans.append(nums[d[x]])
            
        return ans