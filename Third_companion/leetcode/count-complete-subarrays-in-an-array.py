class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        v = len(set(nums))
        ct = 0
        for x in range(N):
            s = set()
            for y in range(x, N):
                s.add(nums[y])
                if len(s) == v:
                    ct += 1
                elif len(s)>v:
                    break
        return ct