class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ct  = 0
        d = defaultdict(int)
        d[0] = 1
        s = 0
        for x in nums:
            s += x
            if s-goal in d:
                ct += d[s-goal]
            d[s] += 1
        return ct
