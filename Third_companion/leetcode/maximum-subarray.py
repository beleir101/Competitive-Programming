class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10**6
        curr = 0
        for x in nums:
            curr = max(curr+x, x)
            ans = max(curr,ans)
        return ans