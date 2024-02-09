class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0]=1
        s = 0
        tt = 0
        for x in nums:
            s += x
            if s - k in d:
                tt += d[s-k]
            d[s] += 1
        return tt