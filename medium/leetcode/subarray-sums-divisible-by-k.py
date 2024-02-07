class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        sums = 0
        ways = 0
        for i in nums:
            sums += i
            if sums%k in d:
                ways += d[sums%k]
            d[sums%k] += 1
        return ways