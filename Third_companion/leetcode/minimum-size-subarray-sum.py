class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        rs = 0
        i,j = 0,0
        mn = float('inf')
        while j < N:
            rs += nums[j]
            while rs >= target and i <= j:
                mn = min(mn, j-i+1)
                rs -= nums[i]
                i += 1
            if mn == 1:
                break
            j += 1
        if mn == float('inf'):
            return 0
        return mn