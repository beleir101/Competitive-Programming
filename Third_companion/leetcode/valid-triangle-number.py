class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return 0
        ans = 0
        nums.sort()
        for x in range(2, N):
            r = 0
            j = x-1
            while r < j:
                if nums[r]+nums[j]> nums[x]:
                    ans += j-r
                    j -= 1
                else:
                    r += 1
        return ans